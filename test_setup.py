#!/usr/bin/env python3
"""
Test script for GenAI Linux Agent
Run this to verify the setup is working
"""

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

def test_imports():
    """Test if all required modules can be imported"""
    try:
        from app.main import app
        from app.agent_core import plan_actions, apply_actions
        from app.llm_gemini import call_gemini
        from app.policy import load_policy
        from app.state import save_pending, load_pending
        from app.audit import audit_log
        print("✅ All modules imported successfully")
        return True
    except ImportError as e:
        print(f"❌ Import error: {e}")
        return False

def test_config():
    """Test if configuration files can be loaded"""
    try:
        import yaml
        with open("config.yaml") as f:
            config = yaml.safe_load(f)
        print("✅ Configuration loaded successfully")
        return True
    except Exception as e:
        print(f"❌ Config error: {e}")
        return False

def test_policy():
    """Test if policy file can be loaded"""
    try:
        from app.policy import POL
        print("✅ Policy loaded successfully")
        return True
    except Exception as e:
        print(f"❌ Policy error: {e}")
        return False

def test_env():
    """Test if .env file exists"""
    if os.path.exists(".env"):
        print("✅ .env file exists")
        return True
    else:
        print("⚠️  .env file not found - you'll need to create it")
        return False

if __name__ == "__main__":
    print("🧪 Testing GenAI Linux Agent setup...\n")
    
    tests = [
        ("Module Imports", test_imports),
        ("Configuration", test_config),
        ("Policy", test_policy),
        ("Environment", test_env),
    ]
    
    passed = 0
    for name, test_func in tests:
        print(f"Testing {name}...")
        if test_func():
            passed += 1
        print()
    
    print(f"📊 Results: {passed}/{len(tests)} tests passed")
    
    if passed == len(tests):
        print("🎉 All tests passed! The agent should work.")
        print("\nNext steps:")
        print("1. Add your Gemini API key to .env file")
        print("2. Run: uvicorn app.main:app --host 127.0.0.1 --port 8001 --reload")
    else:
        print("⚠️  Some tests failed. Check the errors above.")
