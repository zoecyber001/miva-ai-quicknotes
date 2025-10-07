# Miva AI QuickNotes

**AI Study Companion for Online Lectures & PDFs**

Miva AI QuickNotes is a minimal prototype that helps students summarize long video transcripts or PDF text into concise study notes, bullet point highlights, and short quiz questions — designed for fast prototyping at hackathons.

## Why
Online students often rewatch long lectures or re-read dense PDFs. This tool shortens study time by producing focused summaries and practice questions.

## Features (Prototype)
- Paste lecture transcript or text from PDFs
- Get a concise summary (1–3 bullets)
- Generate 3 quick quiz questions
- Lightweight web UI + simple FastAPI backend using the OpenAI API

## Tech stack
- Backend: Python + FastAPI
- Frontend: Static HTML + fetch API
- AI: OpenAI API (via `OPENAI_API_KEY` env var)
- (Optional) Deployable to Heroku / Vercel (backend containerization not included here)

## Quick start (local)
1. Clone repo
2. Create and activate a virtualenv
3. Install dependencies:
```bash
pip install -r requirements.txt
```
4. Create `.env` from `.env.example` and set `OPENAI_API_KEY`
5. Run backend:
```bash
uvicorn backend.main:app --reload
```
6. Open `frontend/index.html` in your browser and test.

## How it works (high-level)
- Frontend posts the text to `/summarize`
- Backend sends a prompt to the OpenAI API to return:
  - A short summary
  - 3 quiz questions
- Backend returns a JSON payload that the frontend displays

## Make it yours (how I used forks)
I explored and learned from multiple open-source tools (ESP, security, and AI examples). This repository is an original prototype demonstrating my AI integration and rapid prototyping skills.

## License
MIT