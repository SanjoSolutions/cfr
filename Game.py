class Game:
    def __init__(self):
        self.players = []

    def add_player(self, agent):
        self.players.append(agent)

    def add_players(self, agents):
        self.players.extend(agents)

    def get_number_of_players(self):
        pass

    def get_all_actions(self):
        pass

    def determine_valid_actions(self):
        pass

    def determine_payoff(self, actions):
        pass

    def play_a_round(self):
        # TODO: Use Round
        actions = tuple(
            player.choose_action(self)
            for player
            in self.players
        )
        result = self.determine_payoff(actions)
        for player in self.players:
            player.receive_result(result)


class Player:
    def choose_action(self, game):
        pass


class Round:
    def is_complete(self):
        pass
