#!/usr/bin/python3


import itertools
from pyrsistent import pset
from scipy.stats import hypergeom

from card import Card

class PokerTools():

    @classmethod
    def gen_deck(self):
        deck = []
        for rank, suit in itertools.product(Card.rank_map, Card.suit_map):
            deck.append(Card(rank, suit))
        return pset(deck)

    @classmethod
    def get_draw_probability(self, state, needed_cards, draws, drawn_at_least=None):
        """
        Given we know the deck size and are counting known cards we can calculate
        the probability of picking _needed_cards_ from the deck when we have
        _draws_ amount of draws to do it and need _drawn_at_least_ amount of cards
        to be drawn.

        Args:
            state (PClass): poker game state object
            needed_cards (set, list, int): cards that we need to draw
            draws (int): amount of tries we have to draw them
            drawn_at_least (int): amount of cards we need to draw (we can have
                multiple outs). Defaulted to len(needed_cards)

        Return:
            probability of drawing the needed cards.
        """
        if isinstance(needed_cards, (set, list, pset)):
            if set(needed_cards) & set(state.revealed_cards):
                return 0
            needed_cards = len(needed_cards)

        drawn_at_least = drawn_at_least or needed_cards
        # pmf(k, M, n, N)
        #   from M cards, n of which are marked, if you randomly choose N cards 
        #   without replacement, exactly k cards will be marked.
        return hypergeom.pmf(drawn_at_least, len(state.deck), needed_cards, draws)



