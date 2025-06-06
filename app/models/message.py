from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
from datetime import datetime
from .base import Base

class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, index=True)
    chat_id = Column(String, index=True)  # Telegram chat ID
    user_id = Column(String, index=True)  # Telegram user ID
    message_text = Column(Text)
    response_text = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Foreign keys
    bot_id = Column(Integer, ForeignKey("bots.id"))
    
    # Relationships
    bot = relationship("Bot", back_populates="messages") 