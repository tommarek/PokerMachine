#!/usr/bin/python

class PokerAction():
    def __str__(self):
        args = {k:getattr(self, k) for k in self.__slots__}
        ret = f"{self.__class__.__name__} {args}"
        return ret

class NoAction(PokerAction):
    __slots__ = []

class ActionDealFlop(PokerAction):
    __slots__ = ['cards']
    def __init__(self, cards):
        self.cards = cards

class ActionAnte(PokerAction):
    __slots__ = ['bet']
    def __init__(self, bet):
        self.bet = bet

class ActionSmallBlind(PokerAction):
    __slots__ = ['pid', 'bet']
    def __init__(self, pid, bet):
        self.bet = bet
        self.pid = pid

class ActionBigBlind(PokerAction):
    __slots__ = ['pid', 'bet']
    def __init__(self, pid, bet):
        self.bet = bet
        self.pid = pid

class ActionFold(PokerAction):
    __slots__ = ['pid']
    def __init__(self, pid):
        self.pid = pid

class ActionCheck(PokerAction):
    __slots__ = ['pid']
    def __init__(self, pid):
        self.pid = pid

class ActionCall(PokerAction):
    __slots__ = ['pid', 'bet']
    def __init__(self, pid, bet):
        self.pid = pid
        self.bet = bet

class ActionRaise(PokerAction):
    __slots__ = ['pid', 'bet']
    def __init__(self, pid, bet):
        self.pid = pid
        self.bet = bet


