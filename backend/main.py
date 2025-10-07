# backend/main.py
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv
from ai_providers import ai_manager

load_dotenv()

app = FastAPI(title="Miva AI QuickNotes API", version="1.0.0")

# Add CORS middleware to allow frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify your frontend domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class TextIn(BaseModel):
    text: str
    max_summary_sentences: int = 3
    provider: str = None  # Optional: override default provider

@app.get("/")
async def root():
    available_providers = list(ai_manager.providers.keys())
    return {
        "message": "Miva AI QuickNotes API is running",
        "available_providers": available_providers,
        "default_provider": ai_manager.default_provider
    }

@app.get("/providers")
async def list_providers():
    """List available AI providers and their models"""
    return {
        "available_providers": ai_manager.get_available_providers(),
        "default_provider": ai_manager.default_provider
    }

@app.post("/summarize")
async def summarize(payload: TextIn):
    text = payload.text.strip()
    if not text:
        raise HTTPException(status_code=400, detail="No text provided")

    # Create the prompt
    prompt = f"""
You are an assistant that creates concise study outputs for university students.
Input: {text}

Output JSON with keys:
- "summary": a 2-3 sentence concise summary
- "key_points": 4 bullet points (short)
- "quiz_questions": 3 short multiple-choice or short-answer questions

Return only valid JSON.
"""

    try:
        result = await ai_manager.generate_summary(prompt, payload.provider)
        return result
        
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"AI Provider Error: {str(e)}")