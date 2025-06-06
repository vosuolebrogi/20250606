from .base import Base, engine, SessionLocal, get_db
from .user import User
from .bot import Bot
from .message import Message
from .analytics import Analytics
from .subscription import Subscription

# Create all tables
Base.metadata.create_all(bind=engine) 