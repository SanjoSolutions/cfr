from enum import IntEnum
from typing import List
import random

from Game import Game, Round


class PokerGame(Game):
    def __init__(self, players, big_blind, small_blind):
        self.players = players
        self.big_blind = big_blind
        self.small_blind = small_blind
        self.number_of_players = len(self.players)
        self.game_specification = {
            'number_of_players': self.number_of_players,
            'number_of_betting_rounds': 2,
            'number_of_board_cards_to_draw': (0, 1,)
        }
        self.dealer_button_position = 0
        self.round = None

    def play_a_round(self):
        self.round = PokerRound(self, self.players, self.dealer_button_position)
        self.round.play()
        self.dealer_button_position = (self.dealer_button_position + 1) % len(self.players)


class PokerTable:
    pass


class PokerDealer:
    pass


class PokerPlayer:
    def __init__(self, stack):
        self.stack = stack
        self.cards = None

    def give_cards(self, cards):
        self.cards = cards

    def choose_action(self, game):
        pass


class PokerRound(Round):
    def __init__(self, game, players, dealer_button_position):
        self.game = game
        self.deck = None
        self.board = []
        self.players = players
        self.players_in_round = list(range(len(self.players)))
        self.amount_in_pot = [0] * len(self.players)
        self.dealer_button_position = dealer_button_position
        self.players_in_round_index_to_act = None
        self.betting_rounds = []
        self.betting_round_index = None

    def play(self):
        for betting_round_index in range(self.game.game_specification['number_of_betting_rounds']):
            self.betting_round_index = betting_round_index
            betting_round = PokerBettingRound(self)
            self.betting_rounds.append(betting_round)

            if betting_round_index == 0:
                self.post_blinds()
                self.new_deck()
                self.shuffle_cards()
                self.deal_cards()

            self.draw_public_cards()

            while not self.is_complete():
                self.players_in_round_index_to_act = self.determine_player_to_act_on_round_start()
                player_to_act_index = self.players_in_round[self.players_in_round_index_to_act]
                player_to_act = self.players[player_to_act_index]
                action = player_to_act.choose_action(self)
                action_type, amount = action
                round_action = PokerBettingRoundAction(player_to_act_index, action)
                betting_round.actions.append(round_action)
                if action_type == ActionType.RAISE:
                    betting_round.raiser_position = player_to_act_index
                    betting_round.number_of_calls_after_raise = 0
                elif action_type == ActionType.CALL:
                    betting_round.number_of_calls_after_raise += 1
                elif action_type == ActionType.FOLD:
                    del self.players_in_round[self.players_in_round_index_to_act]

                if action_type in {ActionType.CALL, ActionType.RAISE}:
                    self.players_in_round_index_to_act += 1
                self.players_in_round_index_to_act %= len(self.players_in_round)

            if betting_round_index == self.game.game_specification['number_of_betting_rounds'] - 1:
                self.show_down()

    def post_blinds(self):
        self.amount_in_pot[self.small_blind_position()] += self.game.small_blind
        self.amount_in_pot[self.big_blind_position()] += self.game.big_blind
        self.betting_rounds[0].raiser_position = self.big_blind_position()

    def new_deck(self):
        self.deck = create_deck()

    def shuffle_cards(self):
        self.deck.shuffle()

    def deal_cards(self):
        first_player_to_give_cards_to = (self.dealer_button_position + 1) % len(self.players)
        for offset in range(len(self.players)):
            player_index = (first_player_to_give_cards_to + offset) % len(self.players)
            cards = (self.deck.draw(),)
            self.players[player_index].give_cards(cards)

    def draw_public_cards(self):
        number_of_board_cards_to_draw = \
            self.game.game_specification['number_of_board_cards_to_draw'][self.betting_round_index]
        for i in range(number_of_board_cards_to_draw):
            self.board.append(self.deck.draw())

    def show_down(self):
        pass

    def small_blind_position(self):
        return (self.dealer_button_position + 1) % len(self.players)

    def big_blind_position(self):
        return (self.small_blind_position() + 1) % len(self.players)

    def determine_player_to_act_on_round_start(self):
        position = (self.big_blind_position() + 1) % len(self.players)
        while position not in self.players_in_round:
            position = (position + 1) % len(self.players)
        return position


class Deck:
    def __init__(self, cards):
        self.cards = cards

    def draw(self):
        return self.cards.pop()

    def shuffle(self):
        random.shuffle(self.cards)


class PokerBettingRound:
    def __init__(self, round):
        self.round = round
        self.actions: List[PokerBettingRoundAction] = []
        self.raiser_position = None
        self.number_of_calls_after_raise = 0

    def is_complete(self):
        return (
            len(self.round.players_in_round) <= 1 or
            (
                len(self.actions) >= len(self.round.players) and
                self.number_of_calls_after_raise == len(self.round.players_in_round) - 1
            )
        )


class PokerBettingRoundAction:
    def __init__(self, player, action):
        self.player = player
        self.action = action  # (action_type, amount)


class ActionType(IntEnum):
    FOLD = 0
    CALL = 1
    RAISE = 2


class Card(IntEnum):
    K = 2
    Q = 1
    J = 0


bet_amounts = (
    1,
    2
)


def create_deck():
    return Deck(2 * list(Card))
