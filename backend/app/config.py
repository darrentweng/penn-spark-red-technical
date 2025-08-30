import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    # Database - support both PostgreSQL and SQLite
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./skillswap.db")
    
    # JWT
    SECRET_KEY: str = os.getenv("SECRET_KEY", "your-secret-key-here")
    ALGORITHM: str = os.getenv("ALGORITHM", "HS256")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "30"))
    
    # App
    DEBUG: bool = os.getenv("DEBUG", "True").lower() == "true"
    
    @property
    def is_sqlite(self) -> bool:
        """Check if using SQLite database."""
        return self.DATABASE_URL.startswith("sqlite")

settings = Settings()

