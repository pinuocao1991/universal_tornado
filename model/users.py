from sqlalchemy import Column, Integer, String

from model.aa_gogogo import Base

class User(Base):  # 继承生成的orm基类
    __tablename__ = "sql_test"  # 表名
    id = Column(Integer, primary_key=True)  # 设置主键
    user_name = Column(String(32))
    user_password = Column(String(64))
