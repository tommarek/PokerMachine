#!/usr/bin/python

from const import Action

class PokerAction():
    def __init__(self):
        pass

class ActionForcedBet(PokerAction):
    action = Action.ANTE
    def __init__(self, bet):
        self.bet = amount

class ActionSmallBlind(PokerAction):
    action = Action.SMALL_BLIND
    def __init__(self, player, bet):
        self.bet = bet
        self.player = player

class ActionBigBlind(PokerAction):
    action = Action.BIG_BLIND
    def __init__(self, player, bet):
        self.bet = bet
        self.player = player

class ActionFold(PokerAction):
    action = Action.FOLD
    def __init__(self, player):
        self.player = player

class ActionCall(PokerAction):
    action = Action.CALL
    def __init__(self, player, bet):
        self.player = player
        self.bet = bet

class ActionRaise(PokerAction):
    action = Action.RAISE
    def __init__(self, player, bet):
        self.player = player
        self.bet = bet

class ActionSitOut(PokerAction):
    action = Action.SIT_OUT
    def __init__(self, player):
        self.player = player


