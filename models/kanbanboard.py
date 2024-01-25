from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class KanbanBoard(Base):
    __tablename__ = 'KanbanBoards'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=True)
    description = Column(Text)
    user_email = Column(String(100), ForeignKey('user.email'), nullable=False)

    # Relacionamento com User e KanbanCard
    user = relationship("User", back_populates="kanbanboards")
    tarefas = relationship("KanbanCard", back_populates="kanbanboard")
    backlogs = relationship("Backlog", back_populates="kanbanboard")
