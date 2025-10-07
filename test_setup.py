#!/usr/bin/env python3
"""
Quick test script to verify the multi-provider setup without API calls
"""

import os
import sys

def test_imports():
    """Test that all imports work correctly"""
    try:
        print("Testing imports...")
        
        # Test FastAPI imports
        from fastapi import FastAPI
        print("✅ FastAPI imports work")
        
        # Test that our modules can be imported
        sys.path.insert(0, './backend')
        from ai_providers import AIProviderManager
        print("✅ AI Provider Manager can be imported")
        
        # Test basic initialization
        os.environ['AI_PROVIDER'] = 'openai'  # Set default
        manager = AIProviderManager()
        print(f"✅ Manager initialized successfully")
        print(f"   Default provider: {manager.default_provider}")
        print(f"   Available providers: {list(manager.providers.keys()) or 'None (no API keys configured)'}")
        
        return True
    except ImportError as e:
        print(f"❌ Import error: {e}")
        print("   Run: pip install -r requirements.txt")
        return False
    except Exception as e:
        print(f"❌ Setup error: {e}")
        return False

def test_frontend():
    """Check that frontend files exist"""
    try:
        with open('./frontend/index.html', 'r') as f:
            content = f.read()
            if 'providerSelect' in content:
                print("✅ Frontend has multi-provider UI")
            else:
                print("❌ Frontend missing provider selection")
                return False
        return True
    except FileNotFoundError:
        print("❌ Frontend file not found")
        return False

def main():
    print("🧪 Testing Miva AI QuickNotes Multi-Provider Setup\n")
    
    # Test project structure
    required_files = [
        'README.md', 'requirements.txt', '.gitignore',
        'backend/main.py', 'backend/ai_providers.py', 'backend/.env.example',
        'frontend/index.html'
    ]
    
    print("📁 Checking project structure...")
    for file in required_files:
        if os.path.exists(file):
            print(f"✅ {file}")
        else:
            print(f"❌ {file} missing")
            return False
    
    print("\n🔌 Testing imports...")
    imports_ok = test_imports()
    
    print("\n🎨 Testing frontend...")  
    frontend_ok = test_frontend()
    
    print(f"\n{'🎉 Setup looks good!' if imports_ok and frontend_ok else '⚠️  Setup needs attention'}")
    
    if not imports_ok:
        print("\nNext steps:")
        print("1. pip install -r requirements.txt")
        print("2. cp backend/.env.example backend/.env")  
        print("3. Add your AI provider API keys to backend/.env")
        print("4. cd backend && uvicorn main:app --reload")

if __name__ == "__main__":
    main()