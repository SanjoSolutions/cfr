from enum import IntEnum

from GameWithPayoffTable import GameWithPayoffTable
from cfr import cfr


class Action(IntEnum):
    Schere = 0
    Stein = 1
    Papier = 2


payoff_table = (
    # ((p1 action, p2 action), (p1 payoff, p2 payoff))
    ((Action.Schere, Action.Schere), (0, 0)),
    ((Action.Schere, Action.Stein), (-1, 1)),
    ((Action.Schere, Action.Papier), (1, -1)),
    ((Action.Stein, Action.Schere), (1, -1)),
    ((Action.Stein, Action.Stein), (0, 0)),
    ((Action.Stein, Action.Papier), (-1, 1)),
    ((Action.Papier, Action.Schere), (-1, 1)),
    ((Action.Papier, Action.Stein), (1, -1)),
    ((Action.Papier, Action.Papier), (0, 0)),
)


if __name__ == '__main__':
    game = GameWithPayoffTable({
        'number_of_players': 2,
        'actions': list(Action),
        'payoffs': payoff_table,
    })
    number_of_iterations = 1000000
    strategies = cfr(game, number_of_iterations)
    print('strategies', strategies)
