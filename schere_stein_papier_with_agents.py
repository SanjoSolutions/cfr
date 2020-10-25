from GameWithAgentsAndPayoffTable import GameWithAgentsAndPayoffTable
from cfr import cfr_with_agents, CFRAgent
from schere_stein_papier import Action, payoff_table

if __name__ == '__main__':
    game_specification = {
        'number_of_players': 2,
        'actions': list(Action),
        'payoffs': payoff_table,
    }
    agents = tuple(
        CFRAgent(game_specification, agent_index)
        for agent_index
        in range(game_specification['number_of_players'])
    )
    game = GameWithAgentsAndPayoffTable(
        game_specification,
        agents
    )
    number_of_iterations = 1000000
    strategies = cfr_with_agents(game, number_of_iterations)
    print('strategies', strategies)
