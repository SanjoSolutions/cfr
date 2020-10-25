from Game import Game


class GameWithAgents(Game):
    def __init__(self, game_specification, agents):
        self.game_specification = game_specification
        self.agents = agents

    def play_a_round(self):
        actions = tuple(
            agent.choose_action(self)
            for agent
            in self.agents
        )
        result = self.determine_payoff(actions)
        for agent in self.agents:
            agent.receive_result(result)
