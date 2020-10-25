from Game import Player
from cfr import CFRLearningAgent
from create_game import create_game
from game_cfr import game_cfr_main
from schere_stein_papier_brunnen.players_2 import SchereSteinPapierBrunnen, payoff_table


class SchereSteinPapierBrunnenPlayer(CFRLearningAgent, Player):
    def __init__(self, agent_index, game: SchereSteinPapierBrunnen, regret=None, strategy=None):
        super().__init__(agent_index, game, regret, strategy)


def schere_stein_papier_brunnen_main(number_of_players, payoff_table):
    game = create_game(
        SchereSteinPapierBrunnen,
        SchereSteinPapierBrunnenPlayer,
        number_of_players=number_of_players,
        payoff_table=payoff_table
    )
    game_cfr_main(game, number_of_iterations=2000000)


if __name__ == '__main__':
    schere_stein_papier_brunnen_main(number_of_players=2, payoff_table=payoff_table)
