import random


class Deck:
    def __init__(self):
        self.denomination = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
        self.suit = ["♠", "♥", "♣", "♦"]
        deck = {}
        for x in self.suit:
            itt = 0
            for y in self.denomination:
                deck.update({f"{y}{x}": values[itt]})
                itt += 1
        self.__deck = deck

    def set_deck(self):
        return list(self.__deck.keys())

    """def shuffled_deck(self):
        random.shuffle(self.set_deck())"""

    def get_card_value(self, card):
        return self.__deck.get(card, 0)

    def set_dummy_data(self):
        return self.set_deck()


class Combinations:
    """ def __init__(self, args):
            self.result = {}
            for x in [self.high_card, self.pair]:
                data = x()
                self.result.update({data[0]: data[1]})

        def __str__(self):
            return self.result
            """

    def sorted_data(self, args):
        data = ''.join(args)
        n = []
        t = []
        counter = 0
        for x in data:
            if x == '1':
                n.append('10')
                counter += 2
                continue
            if counter % 2 != 0:
                t.append(x)
                counter += 1
            else:
                n.append(x)
                counter += 1
        if '10' in n:
            n.pop(n.index('10') + 1)
        n.sort()
        t.sort()
        return n, t

    def high_card(self, args):
        name = 'high_card'
        value = 1
        pass

    def pair(self, args: list):
        name = 'pair'
        value = 2
        data = self.sorted_data(args)
        result = []
        for x in data[0]:
            result.append(data[0].count(x))
        result.sort()
        if result[-1] == 2:
            return True
        return False

    def two_pair(self, args):
        name = 'two pair'
        value = 3
        data = self.sorted_data(args)
        result = []
        for x in data[0]:
            result.append(data[0].count(x))
        result.sort()
        if result[-1] == 2 and result.count(2) >= 4:
            return True
        return False

    def set(self, args):
        name = 'set'
        value = 4
        data = self.sorted_data(args)
        result = []
        for x in data[0]:
            result.append(data[0].count(x))
        result.sort()
        if result[-1] == 3:
            return True
        return False

    def straight(self, args):
        name = 'straight'
        value = 5
        data = self.sorted_data(args)
        temp = []
        data = data[0]
        for x in data:
            temp.append(Deck().denomination.index(x))
        res = 0
        for x in range(len(temp) - 1):
            if temp[x] + 1 == temp[x + 1]:
                res += 1
        if res >= 4:
            return True
        else:
            return False

    def flush(self, args):
        # made by Alex
        name = "flush"
        value = 6
        data = self.sorted_data(args)
        result = []
        for x in Deck().suit:
            result.append(data[1].count(x))
        result.sort()
        if result[-1] >= 5:
            return True
        else:
            return False

    def full_house(self, args):
        name = 'full house'
        value = 7
        data = self.sorted_data(args)
        result = []
        for x in data[0]:
            result.append(data[0].count(x))
        result.sort()
        if result[-1] == 3 and set(result).__len__() == 3:
            return True
        return False

    def carey(self, *args):
        name = '4 of a kind'
        value = 8
        data = self.sorted_data(args)
        result = []
        for x in data[0]:
            result.append(data[0].count(x))
        result.sort()
        if result[-1] == 4:
            return True
        else:
            return False

    def straight_flush(self, args):
        name = 'Straight Flush'
        value = 9
        result = all([self.straight(args), self.flush(args)])
        return result

    def royal_flush(self, args):
        name = 'Royal Flush'
        value = 10
        data = self.sorted_data(args)
        if_flush = self.flush(args)
        temp = 0
        for x in ["10", 'J', 'Q', 'K', 'A']:
            if x in data[0]:
                temp += 1
        if temp >= 5:
            if_royal = True
        else:
            if_royal = False
        if if_royal and if_flush:
            return True
        else:
            return False


class FileMethods:
    @staticmethod
    def create_room(number):
        file = open(f"games/game#{number}.json", 'w')
        return file
