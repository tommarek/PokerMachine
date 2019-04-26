#!/usr/bin/python

from pyrsistent import field, PClass, pvector, pvector_field, pset, pset_field

from player_actions import (
    ActionForcedBet,
    ActionSmallBlind,
    ActionBigBlind,
    ActionFold,
    ActionCall,
    ActionRaise,
    ActionSitOut,
    PokerAction,
)
from card import Card
from const import Action, Street, PLAYER_STATS
from player import Player
from player_manager import PlayerManager

class PlayerState():
    def __init__(self, pid, stack, position=None, player=None):
        self.pid = pid
        self.stack = stack
        self.position = position
        self.playing = True
        self.cards = None
        self.active_bet = None
        self.stats = self.load_stats(player)

    @property
    def is_all_in(self):
        return True if self.playing and stack == 0 and active_bet else False

    def load_stats(self, player):
        stats = {}
        if player:
            for stat in PLAYER_STATS:
                stats[stat] = player.get(stat)
            stats['hand_count'] = player.hand_count
        return stats

    def store_statistics(self):
        pass


class GameState(PClass):
    street = field(type=Street, initial=Street.PREFLOP)
    board = pset_field(item_type=Card, optional=True)
    action = field(type=Action, initial=Action.NOACTION)
    players = pvector_field(item_type=PlayerState)
    pot = field(type=int, initial=0)



class PokerGame():
    """
    This class handles all changes that happen to the game state during a single
    hand played.
    """

    def __init__(self, player_manager):
        self.state = GameState()
        self._history = []
        self.player_manager = player_manager

    def __str__(self):
        ret = "PokerGame:\n"
        ret += "\tGameState:\n"
        ret += f"\t\tstreet: {self.state.street}\n"
        ret += f"\t\tboard: {self.state.board}\n"
        ret += f"\t\tpot: {self.state.pot}\n"
        ret += f"\t\taction: {self.state.action}\n"
        ret += f"\t\thistory: {len(self._history)}\n"
        ret += "\tPlayers:\n"
        if len(self.state.players):
            for player in self.state.players:
                ret += f"\t\tPID: '{player.pid}' (Playing:{player.playing})\n"
                ret += f"\t\t\tstack: {str(player.stack)}\n"
                ret += f"\t\t\tactive_bet: {player.active_bet}\n"
        else:
            ret += "\t\tNo players"

        return ret

    def _update_state(self, changes):
        """
        update changes according to changes in argument
        Attrs:
            changes(dict): key/val with changes to state class

        Returns:
            new state
        """
        self._history.append(self.state)
        new_state = self.state

        for key, val in changes.items():
            new_state = new_state.set(key, val)
        self.state = new_state

    def deal_flop(self, cards):
        self._update_state({"board": pset(cards), "street": Street.FLOP})

    def deal_card(self, card):
        new_board = self.state.board.add(card)
        new_street = self.state.street + 1
        self._update_state({"board": new_board, "street": new_street})


    def add_players(self, players_info):
        """
        Add player to players dict and set their bet to 0
        Players need to be added in order - dealer, sb, bb, ...
        Attrs:
            player_info (dict): player info in current game
                {"server:player_name": stack_val}

        """
        players = pvector()
        for pos, player_info in enumerate(players_info):
            player = pm.get_player(player_info['pid'])
            #here we should alos set the stats
            players = players.append(
                PlayerState(
                    pid=player_info['pid'],
                    stack=player_info['stack'],
                    position=pos,
                )
            )

        self._update_state({"board": None, "street": Street.PREFLOP, "players": players})

    def do_forced_bet(self, player):
        self.players[player] += self.ante
        player.bet(self.ante)

    def do_deal_a_card(self, card):
        self.board.append(card)

    def do_player_bet(self, player, amount):
        self.players[player] += self.ante

    def do_player_check(self, player):
        pass

    def do_player_fold(self, player):
        pass

    def add_incident(self, action):
        pass


if __name__ == "__main__":
    pm = PlayerManager('db.sqlite3')
    game = PokerGame(pm)
    players = [
        {'pid': 'ps:p1', 'stack': 1001},
        {'pid': 'ps:p2', 'stack': 1002},
        {'pid': 'ps:p3', 'stack': 1003},
        {'pid': 'ps:p4', 'stack': 1004},
        {'pid': 'ps:p5', 'stack': 1005},
    ]
    game.add_players(players)
    flop = [
        Card(rank=2, suit=2),
        Card(rank=14, suit=3),
        Card(rank=10, suit=2),
    ]
    game.deal_flop(flop)
    print(game)

    pass
















    pass
