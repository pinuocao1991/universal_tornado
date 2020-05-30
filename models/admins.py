from sqlalchemy import Column,Integer,String,create_engine,Text

from models import Base


class admin(Base):
    __tablename__ ='user'
    id = Column(Integer,primary_key=True)
    username = Column(String(20),nullable=False)
    age=Column(Integer,nullable=True)