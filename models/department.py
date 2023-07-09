from sqlalchemy import Column , Integer , String 
from . base import Base


class Department(Base):
    __tablename__ = 'departments'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False )
