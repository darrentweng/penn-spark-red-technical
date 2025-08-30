from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .api import auth, skills, users
from .database import engine
from . import models

# Create database tables
models.Base.metadata.create_all(bind=engine)

# Create FastAPI app
app = FastAPI(
    title="SkillSwap API",
    description="A peer-to-peer microlearning and mentorship platform",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure this properly for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routers
app.include_router(auth.router)
app.include_router(skills.router)
app.include_router(users.router)

@app.get("/")
def read_root():
    """Root endpoint."""
    return {
        "message": "Welcome to SkillSwap API",
        "version": "1.0.0",
        "docs": "/docs"
    }

@app.get("/health")
def health_check():
    """Health check endpoint."""
    return {"status": "healthy"}

