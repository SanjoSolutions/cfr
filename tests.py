import unittest

from cfr import determine_payoff, generate_payoff_dictionary
from schere_stein_papier_brunnen import Action, payoff_table


class Tests(unittest.TestCase):
    def test_determine_payoff(self):
        actions = (Action.Schere, Action.Brunnen)
        payoff_dictionary = generate_payoff_dictionary(payoff_table)
        payoff = determine_payoff(payoff_dictionary, actions)
        self.assertEqual(payoff, (-1, 1))


if __name__ == '__main__':
    unittest.main()
