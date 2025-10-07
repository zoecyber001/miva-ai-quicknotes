# backend/main.py
import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")

if not OPENAI_API_KEY:
    raise RuntimeError("Set OPENAI_API_KEY in environment")

client = OpenAI(api_key=OPENAI_API_KEY)

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

@app.get("/")
async def root():
    return {"message": "Miva AI QuickNotes API is running"}

@app.post("/summarize")
async def summarize(payload: TextIn):
    text = payload.text.strip()
    if not text:
        raise HTTPException(status_code=400, detail="No text provided")

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
        response = client.chat.completions.create(
            model=MODEL,
            messages=[
                {"role": "system", "content": "You produce concise study notes and quiz questions."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=400,
            temperature=0.2,
        )
        answer = response.choices[0].message.content
        
        # The model should send JSON; try to parse it
        import json
        try:
            data = json.loads(answer)
        except Exception:
            # fallback: wrap raw text
            data = {"raw": answer}
        return data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))