from poker import PokerPlayer, ActionType, PokerGame
from cfr import cfr_with_agents, CFRAgent


class PokerGameCFR(PokerGame):
    def play_a_round(self):
        result = super().play_a_round()
        for player in self.players:
            if 'receive_result' in player:
                agent = player
                agent.receive_result(result)


class PokerCFRAgent(PokerPlayer, CFRAgent):
    def __init__(self, game_specification, agent_index, regret=None, strategy=None):
        super(PokerCFRAgent).__init__()
        super(PokerPlayer).__init__(game_specification, agent_index, regret, strategy)

    def choose_action(self, game):
        return super(CFRAgent).choose_action(game)


if __name__ == '__main__':
    game_specification = {
        'number_of_players': 2,
        'actions': list(ActionType)
    }
    agents = tuple(
        PokerCFRAgent(game_specification, agent_index)
        for agent_index
        in range(game_specification['number_of_players'])
    )
    game = PokerGame(agents, big_blind=20, small_blind=10)
    number_of_iterations = 1
    strategies = cfr_with_agents(game, number_of_iterations)
    print('strategies', strategies)
