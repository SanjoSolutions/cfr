from enum import IntEnum

from GameWithPayoffTable import GameWithPayoffTable


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


class SchereSteinPapierBrunnen(GameWithPayoffTable):
    def __init__(self, number_of_players, payoff_table):
        super().__init__(payoff_table)
        self.number_of_players = number_of_players

    def get_number_of_players(self):
        return self.number_of_players

    def get_all_actions(self):
        return list(Action)

    def determine_valid_actions(self):
        return self.get_all_actions()
