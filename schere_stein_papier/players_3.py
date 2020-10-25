from schere_stein_papier.players_2 import Action


payoff_table = (
    # ((p1 action, p2 action, p3 action), (p1 payoff, p2 payoff, p3 payoff))
    ((Action.Schere, Action.Schere, Action.Schere), (0, 0, 0)),
    ((Action.Schere, Action.Schere, Action.Stein), (-1, -1, 2)),
    ((Action.Schere, Action.Schere, Action.Papier), (0.5, 0.5, -1)),
    ((Action.Schere, Action.Stein, Action.Schere), (-1, 2, -1)),
    ((Action.Schere, Action.Stein, Action.Stein), (-1, 0.5, 0.5)),
    ((Action.Schere, Action.Stein, Action.Papier), (0, 0, 0)),
    ((Action.Schere, Action.Papier, Action.Schere), (0.5, -1, 0.5)),
    ((Action.Schere, Action.Papier, Action.Stein), (0, 0, 0)),
    ((Action.Schere, Action.Papier, Action.Papier), (2, -1, -1)),
    ((Action.Stein, Action.Schere, Action.Schere), (2, -1, -1)),
    ((Action.Stein, Action.Schere, Action.Stein), (0.5, -1, 0.5)),
    ((Action.Stein, Action.Schere, Action.Papier), (0, 0, 0)),
    ((Action.Stein, Action.Stein, Action.Schere), (0.5, 0.5, -1)),
    ((Action.Stein, Action.Stein, Action.Stein), (0, 0, 0)),
    ((Action.Stein, Action.Stein, Action.Papier), (-1, -1, 2)),
    ((Action.Stein, Action.Papier, Action.Schere), (0, 0, 0)),
    ((Action.Stein, Action.Papier, Action.Stein), (-1, 2, -1)),
    ((Action.Stein, Action.Papier, Action.Papier), (-1, 0.5, 0.5)),
    ((Action.Papier, Action.Schere, Action.Schere), (-1, 0.5, 0.5)),
    ((Action.Papier, Action.Schere, Action.Stein), (0, 0, 0)),
    ((Action.Papier, Action.Schere, Action.Papier), (-1, 2, -1)),
    ((Action.Papier, Action.Stein, Action.Schere), (0, 0, 0)),
    ((Action.Papier, Action.Stein, Action.Stein), (2, -1, -1)),
    ((Action.Papier, Action.Stein, Action.Papier), (0.5, -1, 0.5)),
    ((Action.Papier, Action.Papier, Action.Schere), (-1, -1, 2)),
    ((Action.Papier, Action.Papier, Action.Stein), (0.5, 0.5, -1)),
    ((Action.Papier, Action.Papier, Action.Papier), (0, 0, 0)),
)
