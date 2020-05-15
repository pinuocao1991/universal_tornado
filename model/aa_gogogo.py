# -*- coding:utf-8 -*-

__author__ = "lili"

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
engine = create_engine("mysql+pymysql://root:123456@127.0.0.1:3306/tornadoDemo", encoding="utf-8", echo=True, max_overflow=5)
# 连接mysql数据库，echo为是否打印结果
Base = declarative_base()  # 生成orm基类

Base.metadata.create_all(engine)  # 创建表结构
