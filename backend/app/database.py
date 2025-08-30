from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings
import os

# Create database engine based on configuration
if settings.is_sqlite:
    # SQLite configuration
    engine = create_engine(
        settings.DATABASE_URL,
        connect_args={"check_same_thread": False}  # Required for SQLite
    )
else:
    # PostgreSQL configuration
    try:
        import psycopg2
        # Use psycopg2 (synchronous)
        engine = create_engine(settings.DATABASE_URL)
    except ImportError:
        # Fallback to asyncpg (asynchronous)
        if settings.DATABASE_URL.startswith("postgresql://"):
            async_url = settings.DATABASE_URL.replace("postgresql://", "postgresql+asyncpg://", 1)
            engine = create_engine(async_url)
        else:
            engine = create_engine(settings.DATABASE_URL)

# Create SessionLocal class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create Base class for models
Base = declarative_base()

# Dependency to get database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

