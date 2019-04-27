#!/usr/bin/python3

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

PLAYER_STATS = ['vpip', 'pfr']

Base = declarative_base()

class Player(Base):
    __tablename__ = "player"
    pid = Column(String, primary_key=True)

    #stats
    hand_count = Column(Integer, nullable=True, default=0)
    vpip = Column(Integer, nullable=True)
    pfr = Column(Integer, nullable=True)
