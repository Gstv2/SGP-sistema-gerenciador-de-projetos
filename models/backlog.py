from sqlalchemy import Column, Integer, String, Text, Date
from sqlalchemy.orm import relationship
from .base import Base

class Backlog(Base):
    __tablename__ = 'backlog'

    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=True)
    description = Column(Text, nullable=True)
    date = Column(Date, nullable=True)