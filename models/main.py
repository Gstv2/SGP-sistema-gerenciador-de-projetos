from sqlalchemy import create_engine 
from sqlalchemy .orm import sessionmaker 
from models . base import Base 
from models . department import Department 
from models . employee import Employee 
from urllib . parse import quote_plus

user =  'user09'  
password = quote_plus ( 'ted@0203  ') 
host = '139.144.26.210  '
port = '3306' 
database = 'db equipe09 '

connection_string = f'mysql://{user}:{password}@{host}:{port}/{database}'
engine = create_engine( connection_string )

Base.metadata.create_all ( engine ) 
print("Tabelas criadas com sucesso !")

Session = sessionmaker (bind=engine ) 
session = Session ()

hr_department = Department(name='Recursos Humanos ' ) 
session.add( hr_department )

