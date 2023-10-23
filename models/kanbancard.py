from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class KanbanCard(Base):
    __tablename__ = 'KanbanCard'

    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=True)
    description = Column(Text, nullable=True)
    status = Column(String(255), nullable=True)
    KanbanBoards_id = Column(Integer, ForeignKey('KanbanBoards.id'), nullable=True)
    kanbanboard = relationship("KanbanBoard", back_populates="tarefas")

from .kanbanboard import KanbanBoard  # Mantenha essa importação
