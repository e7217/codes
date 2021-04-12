# coding: utf-8
from sqlalchemy import Column, DateTime, Integer, MetaData, Unicode
from sqlalchemy.schema import FetchedValue
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata



class Xnlog11t(Base):
    __tablename__ = 'xnlog11t'

    id = Column(Integer, primary_key=True, unique=True, server_default=FetchedValue())
    mchcd = Column(Unicode(20))
    ipaddr = Column(Unicode(20))
    status = Column(Unicode(10))
    inputdt = Column(DateTime, nullable=False, server_default=FetchedValue())
    created = Column(DateTime)
