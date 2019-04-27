#!/usr/bin/python

from pyrsistent import field, PClass, pvector, pvector_field, pset, pset_field

from player_actions import (
    ActionAnte,
    ActionSmallBlind,
    ActionBigBlind,
    ActionFold,
    ActionCall,
    ActionCheck,
    ActionRaise,
    ActionDealFlop,
    NoAction,
    PokerAction,
)
from card import Card
from const import Street
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

    def __str__(self):
        ret = f"PID: '{self.pid}' (Playing:{self.playing}) "
        ret += f"stack: {str(self.stack)} "
        ret += f"active_bet: {self.active_bet}"
        ret += "\n"
        return ret

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
    action = field(type=PokerAction, initial=NoAction)
    players = pvector_field(item_type=PlayerState)
    pot = field(type=int, initial=0)

    def __str__(self):
        ret = "GameState:\n"
    deck = pset_field(        ret += f"  Street: {self.street}\n"
        ret += f"  board: {self.board}\n"
        ret += f"  pot: {self.pot}\n"
        ret += f"  action: {self.action}\n"
        return ret


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
        ret = self.state.__str__()
        ret += f"  history: {len(self._history)}\n"
        if len(self.state.players):
            for player in self.state.players:
                ret += player.__str__()
        else:
            ret += "  No players"

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

    def is_street_finished(self):
        ret = True
        #if self.status.action in (Action.CALL, Actson.FOLD) or 
        #for player in self.state.players:

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

        self._update_state({
            "board": None,
            "street": Street.PREFLOP,
            "players": players,
            "action": NoAction()
        })

    def _do_bet(self, action):
        pid, bet = action.pid, action.bet
        players = self.state.players
        pot = self.state.pot + bet
        for i, player in enumerate(players):
            if player.pid == action.pid:
                player.active_bet += bet
                player.stack -= bet
                players = players.set(i, player)
                break
        self._update_state({"players": players, "pot": pot, "action": action})

    def _do_forced_bet(self, action):
        bet = action.bet
        players = self.state.players
        pot = self.state.pot
        for i in range(len(players)):
            player = players[i]
            if player.stack > bet:
                player.active_bet = bet
                pot += bet
                player.stack -= bet
            else:
                player.active_bet = player.stack
                pot += player.stack
                player.stack = 0
            players = players.set(i, player)
        self._update_state({"players": players, "pot": pot, "action": action})


    def _do_deal_flop(self, action):
        self._update_state({"board": pset(action.cards), "street": Street.FLOP, "action": action})

    def do_deal_card(self, action):
        import ipdb; ipdb.set_trace()

        street = self.state.street
        new_board = self.state.board.add(action.card)

        self._update_state({"board": new_board, "action": action})


    def _do_check(self, player):
        pass

    def _do_fold(self, pid):
        players = self.state.players
        for i, player in enumerate(players):
            if player.pid == pid:
                player.playing = False
                players = players.set(i, player)
                break
        self._update_state({"players": players, "action": ActionFold(pid)})


    def add_incident(self, action):
        pass

    def do_action(self, action):
        if isinstance(action, ActionAnte):
            self._do_forced_bet(action)
        elif isinstance(action, (ActionSmallBlind, ActionBigBlind, ActionCall, ActionRaise)):
            self._do_bet(action)
        elif isinstance(action, ActionFold):
            self._do_fold(action)
        elif isinstance(action, ActionCheck):
            self._do_check(action)
        elif isinstance(action, ActionDealFlop):
            self._do_deal_flop(action)
        else:
            #unknwonw anction
            print("unknown action")


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
    # PREFLOP
    game.add_players(players)
    game.do_action(ActionAnte(10))
    game.do_action(ActionSmallBlind('ps:p1', 100))
    game.do_action(ActionBigBlind('ps:p2', 200))
    game.do_action(ActionFold('ps:p3'))
    game.do_action(ActionFold('ps:p4'))
    game.do_action(ActionCall('ps:p5', 200))
    game.do_action(ActionRaise('ps:p1', 300))
    game.do_action(ActionCall('ps:p2', 200))
    game.do_action(ActionCall('ps:p5', 200))

    # FLOP
    flop = [
        Card(rank=2, suit=2),
        Card(rank=14, suit=3),
        Card(rank=10, suit=2),
    ]
    game.do_action(ActionDealFlop(flop))

    print(game)
    pass
















    pass
