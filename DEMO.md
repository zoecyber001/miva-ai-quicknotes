# Multi-Provider AI Demo

## Quick UI Test (No API Keys Needed)

1. Open `frontend/index.html` in your browser
2. See the beautiful interface with provider selection dropdown
3. Backend won't work without API keys, but you can explore the UI

## Full Demo with Multiple AI Providers

### Step 1: Choose Your Provider(s)
Pick one or more AI providers and get their API keys:

**Option A: OpenAI (Most Popular)**
- Go to https://platform.openai.com/api-keys
- Create API key: `sk-proj-...`

**Option B: Google Gemini (Google's Latest)**  
- Go to https://aistudio.google.com/app/apikey
- Create API key: `AIza...`

**Option C: Anthropic Claude (High Quality)**
- Go to https://console.anthropic.com/
- Create API key: `sk-ant-...`

**Option D: OpenRouter (Access Multiple Models)**
- Go to https://openrouter.ai/keys
- Create API key: `sk-or-...`

### Step 2: Configure Environment
```bash
cd miva-ai-quicknotes
cp backend/.env.example backend/.env
```

Edit `backend/.env` and add your keys:
```bash
# Choose your default provider
AI_PROVIDER=openai

# Add the API keys you have
OPENAI_API_KEY=sk-proj-your-key-here
GEMINI_API_KEY=AIza-your-key-here  
ANTHROPIC_API_KEY=sk-ant-your-key-here
OPENROUTER_API_KEY=sk-or-your-key-here

# Optionally customize models
OPENAI_MODEL=gpt-4o-mini
GEMINI_MODEL=gemini-1.5-flash
ANTHROPIC_MODEL=claude-3-haiku-20240307
OPENROUTER_MODEL=meta-llama/llama-3.1-8b-instruct:free
```

### Step 3: Install and Run
```bash
pip install -r requirements.txt
cd backend && uvicorn main:app --reload
```

### Step 4: Test Multi-Provider Support

1. **Open `frontend/index.html` in browser**
2. **Check available providers** - Click "🔄 Check Available" 
3. **Test with sample text:**

```
Machine learning is a subset of artificial intelligence that enables computers to learn 
and make decisions from data without explicit programming. It involves algorithms that 
can identify patterns, make predictions, and improve performance over time. The three 
main types are supervised learning (using labeled data), unsupervised learning 
(finding hidden patterns), and reinforcement learning (learning through trial and error).
```

4. **Try different providers:**
   - Select "OpenAI" → Generate notes
   - Select "Gemini" → Generate notes  
   - Compare the different responses and styles

### Expected Multi-Provider Output

**OpenAI Response:**
```json
{
  "summary": "Machine learning is an AI subset enabling computers to learn from data without explicit programming. It uses algorithms for pattern recognition and predictions, with three main types: supervised, unsupervised, and reinforcement learning.",
  "key_points": [
    "Subset of artificial intelligence focused on learning from data",
    "Uses algorithms for pattern identification and predictions",  
    "Supervised learning uses labeled training data",
    "Reinforcement learning improves through trial and error"
  ],
  "quiz_questions": [
    "What are the three main types of machine learning?",
    "How does supervised learning differ from unsupervised learning?",
    "What enables machine learning algorithms to improve over time?"
  ],
  "_metadata": {
    "provider": "openai",
    "model": "gpt-4o-mini"
  }
}
```

**Gemini Response Style:**
- Often more conversational summaries
- Different question phrasing  
- Unique key point organization

**Claude Response Style:**
- Very structured and academic
- Precise technical language
- Comprehensive question coverage

## Provider Comparison Demo Script

**For Hackathon Demos:**

1. **"Here's the challenge"** - Students need quick summaries from different content sources
2. **"Here's my solution"** - Multi-provider AI with unified interface  
3. **Show provider selection** - "Works with OpenAI, Gemini, Claude, OpenRouter"
4. **Live comparison** - Same text → different providers → show varied outputs
5. **Highlight architecture** - "One API, multiple AI backends, consistent format"

## Pro Tips for Different Providers

- **OpenAI**: Best for consistent JSON formatting
- **Gemini**: Great for creative/conversational summaries  
- **Claude**: Excellent for academic/technical content
- **OpenRouter**: Access to open-source models (cost-effective)

The multi-provider architecture demonstrates enterprise-level AI integration patterns!