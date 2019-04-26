#!/usr/bin/python3

from const import rank_map, suit_map

class Card():
    def __init__(self, rank=None, suit=None, unknown=False):
        """
        Args:
            rank (int): rank of the card (1)2-14
            suit (int): card suit {1:C, 2:D, 3:H, 4:S}
            unknown (bool): card may be unknown
        """
        assert bool(rank and suit) != bool(unknown), "card needs to be defined or marked as unknown"
        assert unknown or rank in rank_map, "invalid card rank {rank}{suit}"
        assert unknown or suit in suit_map, "invalid card suit {rank}{suit}"

        self.unknown = unknown
        self.rank = 14 if rank == 1 else rank
        self.suit = suit

    def __str__(self):
        if self.unknown:
            return "Unknown"
        return f"{rank_map[self.rank]}{suit_map[self.suit]}"

    def __repr__(self):
        return f"{self.rank}{self.suit}"

    def __eq__(self, card):
        if self.unknown and card.unkown:
            return True
        return self.rank == card.rank

    def __lt__(self, card):
        if self.unknown:
            raise
        return self.rank < card.rank

    def __le__(self, card):
        if self.unknown:
            raise
        return self.rank <= card.rank

    def __ne__(self, card):
        if self.unknown:
            raise
        return self.rank != card.rank

    def __ge__(self, card):
        if self.unknown:
            raise
        return self.rank >= card.rank

    def __gt__(self, card):
        if self.unknown:
            raise
        return self.rank > card.rank

    def __hash__(self):
        return hash(str(self))

    @property
    def id(self):
        return int(self.__repr__)

    @classmethod
    def from_id(self, cid):
        rank = cid // 10
        suit = cid - (rank * 10)
        return self(rank, suit)

    @classmethod
    def from_str(self, rank, suit):
        suit = inverse(suit_map)[suit.upper()]
        rank = inverse(rank_map)[rank.upper()]
        return self(rank, suit)
