import random

from LearningAgent import LearningAgent
from Game import Game
from iterate import iterate


class CFRLearningAgent(LearningAgent):
    def __init__(self, agent_index, game: Game, regret=None, strategy=None):
        super().__init__()
        self.agent_index = agent_index
        self.regret = regret if regret else create_initial_regret(game)
        self.strategy = strategy if strategy else regret_to_strategy(self.regret)
        self.action = None

    def choose_action(self, game: Game):
        self.action = choose_action(game, self.strategy)
        return self.action

    def receive_result(self, result):
        payoff = result[self.agent_index]
        regret = -payoff
        if regret > 0:
            self.regret[self.action] += regret
        self.strategy = regret_to_strategy(self.regret)


def create_initial_regret(game):
    return [0.0] * len(game.get_all_actions())


def choose_action(game: Game, strategy):
    action = random.choices(
        game.get_all_actions(),
        weights=determine_weights_for_action(game, strategy)
    )[0]
    return action


def determine_weights_for_action(game, strategy):
    valid_actions = set(game.determine_valid_actions())
    weights = tuple(
        strategy[action_index] if action in valid_actions else 0
        for action_index, action
        in enumerate(game.get_all_actions())
    )
    return weights


def cfr(game, number_of_iterations):
    iterate(
        lambda: cfr_step(game),
        number_of_iterations
    )
    strategies = tuple(
        agent.strategy
        for agent
        in game.players
    )
    return strategies


def cfr_step(game):
    game.play_a_round()


def regret_to_strategy(regret):
    regret_sum = float(sum(regret))
    if regret_sum == 0:
        strategy = [1.0 / len(regret)] * len(regret)
    else:
        strategy = tuple(
            (regret_sum - regret) / regret_sum
            for regret
            in regret
        )
        strategy_sum = float(sum(strategy))
        strategy = tuple(
            value / strategy_sum
            for value
            in strategy
        )
    return strategy


def regrets_to_strategies(regrets):
    number_of_regret_tuples = len(regrets)
    strategies = [None] * number_of_regret_tuples
    for index in range(number_of_regret_tuples):
        regret = regrets[index]
        strategy = regret_to_strategy(regret)
        strategies[index] = strategy
    return strategies
