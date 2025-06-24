from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey, LargeBinary
from sqlalchemy.orm import relationship, declarative_base
import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    telegram_id = Column(Integer, unique=True, index=True)
    streak = Column(Integer, default=0)
    last_practice = Column(DateTime, default=datetime.datetime.utcnow)

    words = relationship("UserWord", back_populates="user")
    settings = relationship("Setting", uselist=False, back_populates="user")

class Word(Base):
    __tablename__ = "words"
    id = Column(Integer, primary_key=True, index=True)
    en = Column(String, unique=True, index=True)
    ru = Column(String, unique=True, index=True)

class UserWord(Base):
    __tablename__ = "user_words"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    word_id = Column(Integer, ForeignKey("words.id"))
    learned_at = Column(DateTime, default=datetime.datetime.utcnow)
    repetition_stage = Column(Integer, default=1)
    image = Column(LargeBinary, nullable=True)

    user = relationship("User", back_populates="words")
    word = relationship("Word")

class Setting(Base):
    __tablename__ = "settings"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    reminder_time = Column(String, default="09:00")

    user = relationship("User", back_populates="settings")
