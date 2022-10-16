def create_deck():
    denomination = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
    values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    suit = ["♠", "♥", "♣", "♦"]
    deck = {}
    for x in suit:
        itt = 0
        for y in denomination:
            deck.update({f"{y}{x}": values[itt]})
            itt += 1
    print(deck)

