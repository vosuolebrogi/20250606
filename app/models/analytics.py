from sqlalchemy import Column, Integer, DateTime, ForeignKey, JSON
from sqlalchemy.orm import relationship
from datetime import datetime
from .base import Base

class Analytics(Base):
    __tablename__ = "analytics"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(DateTime, default=datetime.utcnow)
    metrics = Column(JSON)  # Store various metrics like message count, user count, etc.
    
    # Foreign keys
    bot_id = Column(Integer, ForeignKey("bots.id"))
    
    # Relationships
    bot = relationship("Bot", back_populates="analytics") 