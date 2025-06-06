from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os
from app.core.config import get_settings

# Load environment variables
load_dotenv()

# Get settings
settings = get_settings()

# Create FastAPI app
app = FastAPI(
    title=settings.APP_NAME,
    description="A platform for creating and managing Telegram bots",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": f"Welcome to {settings.APP_NAME}"}

@app.get("/health")
async def health_check():
    """Health check endpoint that verifies environment variables are set"""
    missing_vars = []
    if not settings.OPENAI_API_KEY:
        missing_vars.append("OPENAI_API_KEY")
    if not settings.TELEGRAM_BOT_TOKEN:
        missing_vars.append("TELEGRAM_BOT_TOKEN")
    
    return {
        "status": "healthy" if not missing_vars else "warning",
        "environment": {
            "openai_key_set": bool(settings.OPENAI_API_KEY),
            "telegram_token_set": bool(settings.TELEGRAM_BOT_TOKEN)
        },
        "missing_variables": missing_vars if missing_vars else None
    } 