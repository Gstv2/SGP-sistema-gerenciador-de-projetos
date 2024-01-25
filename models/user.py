from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship
from .base import Base

class User(Base):
    __tablename__ = 'user'

    email = Column(String(100), primary_key=True)
    telefone = Column(Integer, nullable=False)
    nome = Column(String(50), nullable=False)
    senha = Column(String(20), nullable=False)
    idade = Column(Integer, nullable=True)
    biografia = Column(String(1000), nullable=True)
    cargo = Column(String(100), nullable=True)

    # Relacionamento com KanbanBoard
    kanbanboards = relationship("KanbanBoard", back_populates="user")
    backlogs = relationship("Backlog", back_populates="user")
