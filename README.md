# Miva AI QuickNotes

**Multi-Provider AI Study Companion for Online Lectures & PDFs**

Miva AI QuickNotes is a powerful prototype that helps students summarize long video transcripts or PDF text into concise study notes, bullet point highlights, and short quiz questions — with support for **multiple AI providers** including OpenAI, Google Gemini, Anthropic Claude, and OpenRouter.

## Why
Online students often rewatch long lectures or re-read dense PDFs. This tool shortens study time by producing focused summaries and practice questions using your preferred AI provider.

## Features (Prototype)
- 🤖 **Multi-Provider AI Support**: Choose from OpenAI GPT, Google Gemini, Anthropic Claude, or OpenRouter
- 📝 **Smart Summarization**: Paste lecture transcript or text from PDFs
- 🔑 **Key Points Extraction**: Get concise summaries (1–3 bullets) 
- ❓ **Quiz Generation**: Generate 3 quick quiz questions for self-testing
- 🎨 **Beautiful Interface**: Lightweight web UI with provider selection
- ⚡ **Fast API Backend**: Simple FastAPI backend with unified AI interface

## Tech stack
- **Backend**: Python + FastAPI with multi-provider AI integration
- **Frontend**: Static HTML + fetch API with provider selection
- **AI Providers**: OpenAI, Google Gemini, Anthropic Claude, OpenRouter
- **Deployment**: Configurable via environment variables

## Quick start (local)
1. Clone repo
2. Create and activate a virtualenv
3. Install dependencies:
```bash
pip install -r requirements.txt
```
4. Configure at least one AI provider in `.env`:
```bash
cp backend/.env.example backend/.env
# Edit backend/.env and set your preferred API keys:
# OPENAI_API_KEY=sk-your-key
# GEMINI_API_KEY=your-key  
# ANTHROPIC_API_KEY=sk-ant-your-key
# OPENROUTER_API_KEY=sk-or-your-key
```
5. Run backend:
```bash
cd backend && uvicorn main:app --reload
```
6. Open `frontend/index.html` in your browser and test.

## Supported AI Providers

| Provider | Models | Setup |
|----------|--------|-------|
| **OpenAI** | GPT-4o, GPT-4o-mini, GPT-3.5-turbo | Get API key at [platform.openai.com](https://platform.openai.com) |
| **Google Gemini** | Gemini 1.5 Flash, Gemini Pro | Get API key at [AI Studio](https://aistudio.google.com) |
| **Anthropic Claude** | Claude 3 Haiku, Claude 3 Sonnet | Get API key at [console.anthropic.com](https://console.anthropic.com) |
| **OpenRouter** | Llama 3.1, GPT-4, Claude (unified API) | Get API key at [openrouter.ai](https://openrouter.ai) |

## How it works (high-level)
- Frontend posts the text and optional provider selection to `/summarize`
- Backend routes request to the chosen AI provider (OpenAI, Gemini, Claude, or OpenRouter)
- AI provider returns structured JSON with summary, key points, and quiz questions
- Frontend displays beautifully formatted study notes with provider attribution

## API Endpoints
- `GET /` - API status and available providers
- `GET /providers` - List configured AI providers and models  
- `POST /summarize` - Generate study notes (with optional provider parameter)

## Provider Selection
The app automatically detects which providers you have configured and shows them in the UI. You can:
- Use the default provider (set via `AI_PROVIDER` env var)
- Select a specific provider for each request
- See which provider generated each response

## Make it yours
This repository demonstrates practical AI integration patterns and multi-provider architecture. Perfect for learning how to:
- Abstract multiple AI APIs behind a unified interface
- Handle different response formats across providers
- Build scalable AI applications with provider fallbacks
- Create professional UIs for AI-powered tools

## License
MIT