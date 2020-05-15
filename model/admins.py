from sqlalchemy import Column, Integer, String

from model.aa_gogogo import Base


class Admin(Base):
    __tablename__ = "admin"
    id = Column(Integer, primary_key=True)
    username = Column(String(32))
    password = Column(String(64))