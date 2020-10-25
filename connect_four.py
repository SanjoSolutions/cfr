from itertools import product


class FieldState:
    Empty = 0
    Yellow = 1
    Red = 2


WIDTH = 7
HEIGHT = 6


def generate_payoff_table():
    grid_states = product(list(FieldState), repeat=HEIGHT * WIDTH)
    payoffs = dict([
        (grid_state, determine_payoff(grid_states))
        for grid_state
        in grid_states
    ])
    return payoffs

