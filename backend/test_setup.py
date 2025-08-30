#!/usr/bin/env python3
"""
Simple test script to verify the backend setup.
Run this to check if all imports and basic functionality work.
"""

def test_imports():
    """Test if all required modules can be imported."""
    try:
        print("Testing imports...")
        
        # Test core modules
        from app.config import settings
        print("✓ Config imported successfully")
        
        from app.database import get_db, Base
        print("✓ Database imported successfully")
        
        from app.models import User, Skill, Tag, Message
        print("✓ Models imported successfully")
        
        from app.schemas import UserCreate, SkillCreate
        print("✓ Schemas imported successfully")
        
        from app.auth import verify_password, get_password_hash, create_access_token
        print("✓ Auth utilities imported successfully")
        
        from app.dependencies import get_current_user, get_current_active_user
        print("✓ Dependencies imported successfully")
        
        from app.crud import create_user, get_user_by_username
        print("✓ CRUD operations imported successfully")
        
        print("\n🎉 All imports successful! Backend setup is working correctly.")
        return True
        
    except ImportError as e:
        print(f"❌ Import error: {e}")
        return False
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return False

def test_config():
    """Test configuration loading."""
    try:
        from app.config import settings
        print(f"\nConfiguration test:")
        print(f"  Database URL: {settings.DATABASE_URL}")
        print(f"  JWT Algorithm: {settings.ALGORITHM}")
        print(f"  Token Expiry: {settings.ACCESS_TOKEN_EXPIRE_MINUTES} minutes")
        print(f"  Debug Mode: {settings.DEBUG}")
        return True
    except Exception as e:
        print(f"❌ Configuration error: {e}")
        return False

if __name__ == "__main__":
    print("SkillSwap Backend Setup Test")
    print("=" * 40)
    
    success = True
    success &= test_imports()
    success &= test_config()
    
    if success:
        print("\n✅ Backend setup is ready!")
        print("\nNext steps:")
        print("1. Set up your .env file with database credentials")
        print("2. Install dependencies: pip install -r requirements.txt")
        print("3. Run the server: python run.py")
    else:
        print("\n❌ Backend setup has issues. Please check the errors above.")

