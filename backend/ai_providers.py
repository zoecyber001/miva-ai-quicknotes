# backend/ai_providers.py
"""
AI Provider Configuration and Management

This module handles multiple AI providers (OpenAI, Gemini, Anthropic, OpenRouter)
with a unified interface for generating study summaries.
"""

import os
from typing import Dict, Any, Optional
import httpx
import json

# Import AI clients
from openai import OpenAI
try:
    import google.generativeai as genai
except ImportError:
    genai = None

try:
    from anthropic import Anthropic
except ImportError:
    Anthropic = None


class AIProviderManager:
    """Manages multiple AI providers with a unified interface"""
    
    def __init__(self):
        self.providers = {}
        self.default_provider = os.getenv("AI_PROVIDER", "openai").lower()
        self._initialize_providers()
    
    def _initialize_providers(self):
        """Initialize all available AI providers based on environment variables"""
        
        # OpenAI
        if os.getenv("OPENAI_API_KEY"):
            self.providers["openai"] = {
                "client": OpenAI(api_key=os.getenv("OPENAI_API_KEY")),
                "model": os.getenv("OPENAI_MODEL", "gpt-4o-mini"),
                "type": "openai"
            }
        
        # Google Gemini
        if genai and os.getenv("GEMINI_API_KEY"):
            genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
            model_name = os.getenv("GEMINI_MODEL", "gemini-1.5-flash")
            self.providers["gemini"] = {
                "client": genai.GenerativeModel(model_name),
                "model": model_name,
                "type": "gemini"
            }
        
        # Anthropic Claude
        if Anthropic and os.getenv("ANTHROPIC_API_KEY"):
            self.providers["anthropic"] = {
                "client": Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY")),
                "model": os.getenv("ANTHROPIC_MODEL", "claude-3-haiku-20240307"),
                "type": "anthropic"
            }
        
        # OpenRouter
        if os.getenv("OPENROUTER_API_KEY"):
            self.providers["openrouter"] = {
                "api_key": os.getenv("OPENROUTER_API_KEY"),
                "model": os.getenv("OPENROUTER_MODEL", "meta-llama/llama-3.1-8b-instruct:free"),
                "base_url": "https://openrouter.ai/api/v1",
                "type": "openrouter"
            }
    
    def get_available_providers(self) -> Dict[str, Dict[str, Any]]:
        """Return information about available providers"""
        provider_info = {}
        for name, config in self.providers.items():
            provider_info[name] = {
                "model": config["model"],
                "type": config["type"]
            }
            if "base_url" in config:
                provider_info[name]["base_url"] = config["base_url"]
        return provider_info
    
    def is_provider_available(self, provider: str) -> bool:
        """Check if a provider is configured and available"""
        return provider in self.providers
    
    async def generate_summary(self, text: str, provider: Optional[str] = None) -> Dict[str, Any]:
        """Generate study summary using specified provider"""
        if not provider:
            provider = self.default_provider
        
        if not self.is_provider_available(provider):
            available = list(self.providers.keys())
            raise ValueError(f"Provider '{provider}' not available. Available: {available}")
        
        provider_config = self.providers[provider]
        
        # Call appropriate provider method
        if provider == "openai":
            result = await self._call_openai(text, provider_config)
        elif provider == "gemini":
            result = await self._call_gemini(text, provider_config)
        elif provider == "anthropic":
            result = await self._call_anthropic(text, provider_config)
        elif provider == "openrouter":
            result = await self._call_openrouter(text, provider_config)
        else:
            raise ValueError(f"Unsupported provider: {provider}")
        
        # Add metadata
        try:
            parsed_result = json.loads(result)
            parsed_result["_metadata"] = {
                "provider": provider,
                "model": provider_config["model"]
            }
            return parsed_result
        except json.JSONDecodeError:
            return {
                "raw": result,
                "_metadata": {
                    "provider": provider,
                    "model": provider_config["model"],
                    "note": "Response was not valid JSON"
                }
            }
    
    async def _call_openai(self, prompt: str, config: Dict[str, Any]) -> str:
        """Call OpenAI API"""
        response = config["client"].chat.completions.create(
            model=config["model"],
            messages=[
                {"role": "system", "content": "You produce concise study notes and quiz questions."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=400,
            temperature=0.2,
        )
        return response.choices[0].message.content
    
    async def _call_gemini(self, prompt: str, config: Dict[str, Any]) -> str:
        """Call Google Gemini API"""
        response = config["client"].generate_content(prompt)
        return response.text
    
    async def _call_anthropic(self, prompt: str, config: Dict[str, Any]) -> str:
        """Call Anthropic Claude API"""
        response = config["client"].messages.create(
            model=config["model"],
            max_tokens=400,
            temperature=0.2,
            messages=[{"role": "user", "content": prompt}]
        )
        return response.content[0].text
    
    async def _call_openrouter(self, prompt: str, config: Dict[str, Any]) -> str:
        """Call OpenRouter API"""
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{config['base_url']}/chat/completions",
                headers={
                    "Authorization": f"Bearer {config['api_key']}",
                    "Content-Type": "application/json"
                },
                json={
                    "model": config["model"],
                    "messages": [
                        {"role": "system", "content": "You produce concise study notes and quiz questions."},
                        {"role": "user", "content": prompt}
                    ],
                    "max_tokens": 400,
                    "temperature": 0.2
                }
            )
            response.raise_for_status()
            return response.json()["choices"][0]["message"]["content"]


# Create global instance
ai_manager = AIProviderManager()