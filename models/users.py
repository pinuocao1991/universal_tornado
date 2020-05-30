from sqlalchemy import Column,Integer,String,create_engine,Text

from models import Base
print("sssss")

class user(Base):
    __tablename__ ='article'
    id = Column(Integer,primary_key=True)
    title = Column(String(100),nullable=False)
    content = Column(Text, nullable=False)