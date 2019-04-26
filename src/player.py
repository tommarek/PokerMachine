#!/usr/bin/python3

from sqlalchemy import Column, Integer, String

class Player():
    __tablename__ = "player"
    pid = Column(String, primary_key=True)

    #stats
    hand_count = Column(Integer, nullable=True, default=0)
    vpip = Column(Integer, nullable=True)
    pfr = Column(Integer, nullable=True)
