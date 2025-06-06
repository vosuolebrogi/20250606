from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, JSON
from sqlalchemy.orm import relationship
from datetime import datetime
from .base import Base

class Bot(Base):
    __tablename__ = "bots"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    token = Column(String, unique=True)
    type = Column(String)  # GPT, Claude, Gemini, etc.
    settings = Column(JSON)  # Bot-specific settings
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Foreign keys
    owner_id = Column(Integer, ForeignKey("users.id"))
    
    # Relationships
    owner = relationship("User", back_populates="bots")
    messages = relationship("Message", back_populates="bot")
    analytics = relationship("Analytics", back_populates="bot") 