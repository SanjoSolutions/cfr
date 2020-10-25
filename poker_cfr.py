from poker import PokerPlayer, ActionType, PokerGame
from cfr import cfr, CFRLearningAgent


class PokerGameCFR(PokerGame):
    def play_a_round(self):
        result = super().play_a_round()
        for player in self.players:
            if 'receive_result' in player:
                agent = player
                agent.receive_result(result)


class PokerCFRAgent(PokerPlayer, CFRLearningAgent):
    def __init__(self, game_specification, agent_index, stack, regret=None, strategy=None):
        super(PokerCFRAgent).__init__(stack)
        super(PokerPlayer).__init__(game_specification, agent_index, regret, strategy)

    def choose_action(self, game):
        return super(CFRLearningAgent).choose_action(game)


if __name__ == '__main__':
    game_specification = {
        'number_of_players': 2,
        'actions': list(ActionType)
    }
    stack = 1000
    agents = tuple(
        PokerCFRAgent(game_specification, agent_index, stack)
        for agent_index
        in range(game_specification['number_of_players'])
    )
    game = PokerGame(agents, big_blind=10, small_blind=5)
    number_of_iterations = 1
    strategies = cfr(game, number_of_iterations)
    print('strategies', strategies)
