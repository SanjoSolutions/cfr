import random


def cfr(game, number_of_iterations):
    payoff_dictionary = generate_payoff_dictionary(game['payoffs'])

    regrets = tuple(
        [0.0] * len(game['actions'])
        for player
        in range(game['number_of_players'])
    )
    strategies = [None] * game['number_of_players']

    for i in range(number_of_iterations):
        strategies = regrets_to_strategies(regrets)

        actions = [None] * game['number_of_players']
        for player in range(game['number_of_players']):
            strategy = strategies[player]
            actions[player] = random.choices(game['actions'], weights=strategy)[0]

        payoff = determine_payoff(payoff_dictionary, actions)
        for player in range(game['number_of_players']):
            regret = -payoff[player]
            if regret > 0:
                regrets[player][actions[player]] += regret

    strategies = regrets_to_strategies(regrets)
    return strategies


def generate_payoff_dictionary(payoff_table):
    payoff_dictionary = dict()
    for payoff_entry in payoff_table:
        actions = payoff_entry[0]
        payoff = payoff_entry[1]
        dictionary = payoff_dictionary
        for action_index, action in enumerate(actions):
            if action not in dictionary:
                dictionary[action] = dict()
            if action_index == len(actions) - 1:
                dictionary[action] = payoff
            else:
                dictionary = dictionary[action]
    return payoff_dictionary


def determine_payoff(payoff_dictionary, actions):
    value = payoff_dictionary
    for action in actions:
        value = value[action]
    return value


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
