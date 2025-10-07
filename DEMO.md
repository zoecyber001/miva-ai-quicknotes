# Demo Instructions

## Quick Test (Without OpenAI API)

If you want to test the frontend interface without setting up OpenAI API:

1. Open `frontend/index.html` in your browser
2. You'll see the beautiful interface
3. The backend won't work without API key, but you can see the UI

## Full Demo (With OpenAI API)

1. **Get OpenAI API Key**
   - Go to https://platform.openai.com/api-keys
   - Create a new API key

2. **Set up environment**
   ```bash
   cd miva-ai-quicknotes
   cp backend/.env.example backend/.env
   # Edit backend/.env and add: OPENAI_API_KEY=sk-your-key-here
   ```

3. **Install and run**
   ```bash
   pip install -r requirements.txt
   uvicorn backend.main:app --reload
   ```

4. **Test the app**
   - Open `frontend/index.html` in browser
   - Paste sample text like:
   
   ```
   Photosynthesis is the process by which plants convert sunlight into energy. 
   Chloroplasts contain chlorophyll which captures light energy. The process 
   involves two main stages: light reactions and the Calvin cycle. During 
   light reactions, water molecules are split and oxygen is released. The 
   Calvin cycle uses CO2 to produce glucose using the energy from light reactions.
   ```

5. **Expected Output**
   - **Summary**: 2-3 sentences about photosynthesis
   - **Key Points**: 4 bullet points covering main concepts
   - **Quiz Questions**: 3 questions to test understanding

## Sample Expected Output

```json
{
  "summary": "Photosynthesis is the process where plants convert sunlight into energy using chloroplasts. The process involves light reactions that split water and release oxygen, followed by the Calvin cycle that produces glucose from CO2.",
  "key_points": [
    "Chloroplasts contain chlorophyll for capturing light energy",
    "Light reactions split water molecules and release oxygen",
    "Calvin cycle converts CO2 into glucose using light energy",
    "Process has two main stages working together"
  ],
  "quiz_questions": [
    "What organelle contains chlorophyll for photosynthesis?",
    "What are the two main stages of photosynthesis?",
    "What gas is released during the light reactions?"
  ]
}
```