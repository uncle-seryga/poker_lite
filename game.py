import random

import db
import service


class Game:
    def set_game(self, players_ids: list):
        file = service.FileMethods().create_room(db.DB().new_room())
        file_content = {}
        this_deck = service.Deck().set_deck()
        random.shuffle(this_deck)
        players_hands = []
        table = []
        file_content.update({"flop": [this_deck.pop()], "reaver": [this_deck.pop()]})
        for x in range(3):
            table.append(this_deck.pop())
        file_content.update({"table": table})
        for x in players_ids:
            file_content.update({x: [this_deck.pop(), this_deck.pop()]})
        file.write(str(file_content))
        print(file_content)

        """
        JSON File with room settings and game
        :param players_names: list of players names
        :param player_quantity: integer number of players
        :return:
        """
        pass

    def get_players_from_room(self, room_number):
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
