import random

from Agent import Agent
from iterate import iterate


class CFRAgent(Agent):
    def __init__(self, game_specification, agent_index, regret=None, strategy=None):
        self.game_specification = game_specification
        self.agent_index = agent_index
        self.regret = regret if regret else create_initial_regret(game_specification)
        self.strategy = strategy if strategy else regret_to_strategy(self.regret)
        self.action = None

    def choose_action(self, game):
        self.action = random.choices(
            game.game_specification['actions'],
            weights=self.strategy
        )[0]
        return self.action

    def receive_result(self, result):
        payoff = result[self.agent_index]
        regret = -payoff
        if regret > 0:
            self.regret[self.action] += regret
        self.strategy = regret_to_strategy(self.regret)


def create_initial_regret(game_specification):
    return [0.0] * len(game_specification['actions'])


def cfr_with_agents(game, number_of_iterations):
    regrets = tuple(
        create_initial_regret(game.game_specification)
        for player
        in range(game.game_specification['number_of_players'])
    )
    strategies = regrets_to_strategies(regrets)
    agents = tuple(
        CFRAgent(game, agent_index, regret=regrets[agent_index], strategy=strategies[agent_index])
        for agent_index
        in range(game.game_specification['number_of_players'])
    )
    iterate(
        lambda: cfr_with_agents_step(game),
        number_of_iterations
    )
    strategies = tuple(
        agent.strategy
        for agent
        in agents
    )
    return strategies


def cfr_with_agents_step(game):
    game.play_a_round()


def cfr(game, number_of_iterations):
    regrets = tuple(
        [0.0] * len(game.game_specification['actions'])
        for player
        in range(game.game_specification['number_of_players'])
    )
    strategies = regrets_to_strategies(regrets)

    regrets, strategies = iterate(
        lambda args: cfr_step(game, args),
        number_of_iterations,
        (
            regrets,
            strategies
        )
    )

    return strategies


def cfr_step(game, args):
    regrets, strategies = args
    actions = [None] * game.game_specification['number_of_players']
    for player in range(game.game_specification['number_of_players']):
        strategy = strategies[player]
        actions[player] = random.choices(game.game_specification['actions'], weights=strategy)[0]

    payoff = game.determine_payoff(actions)
    for player in range(game.game_specification['number_of_players']):
        regret = -payoff[player]
        if regret > 0:
            regrets[player][actions[player]] += regret

    strategies = regrets_to_strategies(regrets)

    return regrets, strategies


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
