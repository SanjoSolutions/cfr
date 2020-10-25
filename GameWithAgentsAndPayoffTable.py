from GameWithAgents import GameWithAgents
from GameWithPayoffTable import GameWithPayoffTable


class GameWithAgentsAndPayoffTable(GameWithAgents, GameWithPayoffTable):
    def __init__(self, game_specification, agents):
        super(GameWithAgentsAndPayoffTable, self).__init__(game_specification, agents)
        super(GameWithAgents, self).__init__(game_specification)
