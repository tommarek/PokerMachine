#!/usr/bin/python3

class Card():
    rank_map = {2:"2", 3:"3", 4:"4", 5:"5", 6:"6", 7:"7", 8:"8", 9:"9", 10:"T", 11:"J", 12:"Q", 13:"K", 14:"A"}
    suit_map = {1:"C", 2:"D", 3:"H", 4:"S"}

    __slots__ = ['rank', 'suit']

    def __init__(self, rank, suit):
        assert rank in self.rank_map, "invalid card rank {rank}{suit}"
        assert suit in self.suit_map, "invalid card suit {rank}{suit}"

        self.rank = 14 if rank == 1 else rank
        self.suit = suit

    def __str__(self):
        return f"{rank_map[self.rank]}{suit_map[self.suit]}"

    def __repr__(self):
        return f"Card({self.rank}, {self.suit})"

    def __eq__(self, card):
        return self.rank == card.rank

    def __lt__(self, card):
        return self.rank < card.rank

    def __le__(self, card):
        return self.rank <= card.rank

    def __ne__(self, card):
        return self.rank != card.rank

    def __ge__(self, card):
        return self.rank >= card.rank

    def __gt__(self, card):
        return self.rank > card.rank

    def __hash__(self):
        return hash((self.rank, self.suit))

    @property
    def id(self):
        return int(f"{self.rank}{self.suit}")

    @classmethod
    def from_id(self, cid):
        rank = cid // 10
        suit = cid - (rank * 10)
        return self(rank, suit)

    @classmethod
    def from_str(self, rank, suit):
        suit = dict(map(reversed, suit_map))[suit.upper()]
        rank = dict(map(reversed, rank_map))[rank.upper()]
        return self(rank, suit)
