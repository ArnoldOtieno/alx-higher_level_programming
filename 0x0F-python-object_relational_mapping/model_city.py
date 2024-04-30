#!/usr/bin/python3
"""creating a class and objects"""
from sqlalchemy import Column, String, Integer, MetaData, ForeignKey
from model_state import Base

mymetadata = MetaData()


class City(Base):
    """city base class"""
    __tablename__ = "cities"

    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("state_id"), nullable=False)
