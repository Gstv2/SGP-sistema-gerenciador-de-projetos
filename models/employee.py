from sqlalchemy import Column, Integer , String
from sqlalchemy .orm import relationship
from . base import Base 
from . department import Department

class Employee(Base):
    __tablename__ = 'employees '
    
    id = Column( Integer , primary_key=True)
    name = Column( String (50) , nullable=False ) 
    department_id = Column( Integer, ForeignKey( "departments.id" ) , nullable=False )  
    department = relationship (Department)
