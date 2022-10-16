import random


class Deck:
    def __init__(self):
        denomination = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
        values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
        suit = ["♠", "♥", "♣", "♦"]
        deck = {}
        for x in suit:
            itt = 0
            for y in denomination:
                deck.update({f"{y}{x}": values[itt]})
                itt += 1
        self.__deck = deck

    def __set_deck(self):
        return list(self.__deck.keys())

    def shuffled_deck(self):
        return random.shuffle(self.__set_deck())

    def get_card_value(self, card):
        return self.__deck.get(card, 0)

