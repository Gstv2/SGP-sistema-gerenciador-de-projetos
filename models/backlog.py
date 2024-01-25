from sqlalchemy import Column, Integer, String, Text, Date, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class Backlog(Base):
    __tablename__ = 'backlog'

    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=True)
    description = Column(Text, nullable=True)
    date = Column(Date, nullable=True)

    # Relacionamento com User
    user_email = Column(String(100), ForeignKey('user.email'), nullable=False)
    user = relationship("User", back_populates="backlogs")

    # Relacionamento com KanbanBoard
    kanbanboard_id = Column(Integer, ForeignKey('KanbanBoards.id'), nullable=True)
    kanbanboard = relationship("KanbanBoard", back_populates="backlogs")

