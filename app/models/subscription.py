from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from datetime import datetime
from .base import Base

class Subscription(Base):
    __tablename__ = "subscriptions"

    id = Column(Integer, primary_key=True, index=True)
    plan_type = Column(String)  # free, basic, premium, etc.
    start_date = Column(DateTime, default=datetime.utcnow)
    end_date = Column(DateTime)
    is_active = Column(Boolean, default=True)
    
    # Foreign keys
    user_id = Column(Integer, ForeignKey("users.id"))
    
    # Relationships
    user = relationship("User", back_populates="subscriptions") 