#!/usr/bin/python3

from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Player(Base):
    __tablename__ = "player"
    pid = Column(String, primary_key=True)

    #stats
    hand_count = Column(Integer, nullable=True, default=0)
    vpip = Column(Integer, default=0)
    pfr = Column(Integer, default=0)

engine = create_engine('sqlite:///db.sqlite3')
Base.metadata.create_all(engine)

