#!/usr/bin/python

from const import Action

class PokerAction():
    def __init__(self):
        pass

class NoAction(PokerAction):
    action = Action.NOACTION

class ActionDealFlop(PokerAction):
    action = Action.DEALFLOP
    def __init__(self, cards):
        self.cards = cards

class ActionAnte(PokerAction):
    action = Action.ANTE
    def __init__(self, bet):
        self.bet = bet

class ActionSmallBlind(PokerAction):
    action = Action.SMALL_BLIND
    def __init__(self, pid, bet):
        self.bet = bet
        self.pid = pid

class ActionBigBlind(PokerAction):
    action = Action.BIG_BLIND
    def __init__(self, pid, bet):
        self.bet = bet
        self.pid = pid

class ActionFold(PokerAction):
    action = Action.FOLD
    def __init__(self, pid):
        self.pid = pid

class ActionCheck(PokerAction):
    action = Action.CHECK
    def __init__(self, pid):
        self.pid = pid

class ActionCall(PokerAction):
    action = Action.CALL
    def __init__(self, pid, bet):
        self.pid = pid
        self.bet = bet

class ActionRaise(PokerAction):
    action = Action.RAISE
    def __init__(self, pid, bet):
        self.pid = pid
        self.bet = bet


