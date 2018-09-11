from database import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.types import DateTime
from datetime import datetime


class Comment(Base):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True)
    ip = Column(String(64), index=True)
    timestamp = Column(DateTime, index=True, default=datetime.utcnow)
    comment = Column(String(128))

    def __repr__(self):
        return '<Comment {}>'.format(self.ip)
