from enum import IntEnum

from cfr import cfr


class Action(IntEnum):
    Schere = 0
    Stein = 1
    Papier = 2
    Brunnen = 3


payoff_table = (
    # ((p1 action, p2 action), (p1 payoff, p2 payoff))
    ((Action.Schere, Action.Schere), (0, 0)),
    ((Action.Schere, Action.Stein), (-1, 1)),
    ((Action.Schere, Action.Papier), (1, -1)),
    ((Action.Schere, Action.Brunnen), (-1, 1)),
    ((Action.Stein, Action.Schere), (1, -1)),
    ((Action.Stein, Action.Stein), (0, 0)),
    ((Action.Stein, Action.Papier), (-1, 1)),
    ((Action.Stein, Action.Brunnen), (-1, 1)),
    ((Action.Papier, Action.Schere), (-1, 1)),
    ((Action.Papier, Action.Stein), (1, -1)),
    ((Action.Papier, Action.Papier), (0, 0)),
    ((Action.Papier, Action.Brunnen), (1, -1)),
    ((Action.Brunnen, Action.Schere), (1, -1)),
    ((Action.Brunnen, Action.Stein), (1, -1)),
    ((Action.Brunnen, Action.Papier), (-1, 1)),
    ((Action.Brunnen, Action.Brunnen), (0, 0)),
)


if __name__ == '__main__':
    game = {
        'number_of_players': 2,
        'actions': list(Action),
        'payoffs': payoff_table,
    }
    number_of_iterations = 2000000
    strategies = cfr(game, number_of_iterations)
    print('strategies', strategies)
