from cfr import cfr


def game_cfr_main(game, number_of_iterations):
    strategies = cfr(game, number_of_iterations)
    print('strategies', strategies)
    return strategies
