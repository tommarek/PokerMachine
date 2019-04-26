#!/usr/bin/python3

from enum import Enum

class Suits(Enum):
    CLUB = 1
    DIAMOND = 2
    HEART = 3
    SPADE = 4

class Action(Enum):
    ANTE = 0
    SMALL_BLIND = 1
    BIG_BLIND = 2
    FOLD = 3
    CALL = 4
    RAISE = 5
    SIT_OUT = 6
    NOACTION = 7

class Street(Enum):
    PREFLOP = 0
    FLOP = 1
    TURN = 2
    RIVER = 3
    SHOWDOWN = 4
    ENDED = 5

rank_map = {2:"2", 3:"3", 4:"4", 5:"5", 6:"6", 7:"7", 8:"8", 9:"9", 10:"T", 11:"J", 12:"Q", 13:"K", 14:"A"}
suit_map = {1:"C", 2:"D", 3:"H", 4:"S"}

PLAYER_STATS = ["pfr, vpip"]

