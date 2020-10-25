from Game import Game


class GameWithPayoffTable(Game):
    def __init__(self, payoff_table):
        super().__init__()
        self.payoff_dictionary = generate_payoff_dictionary(payoff_table)

    def determine_payoff(self, actions):
        return determine_payoff(self.payoff_dictionary, actions)


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
