import random

import service


class Game:
    def set_game(self, player_quantity: int, players_names: list):
        this_deck = service.Deck().set_deck()
        random.shuffle(this_deck)
        players_hands = []
        table, flop, reaver = [], [this_deck.pop()], [this_deck.pop()]
        for x in range(3):
            table.append(this_deck.pop())
        for x in range(player_quantity):
            players_hands.append([this_deck.pop(), this_deck.pop()])
        print(table, flop, reaver, players_hands)


        """
        JSON File with room settings and game
        :param players_names: list of players names
        :param player_quantity: integer number of players
        :return:
        """
        pass

    def check_if_combination(self):
        """
        Check rules at PDF file
        :return:
        """

    def check_if_win(self, *players):
        pass


class Bets:
    def set_bet(self):
        pass

    def pass_turn(self):
        pass

    def skip_turn(self):
        pass


class Bank:
    def append_bank(self, *bets):
        pass

    def pay_bank(self, *players):
        pass
