import service
import random

dummy_data = service.Deck().set_dummy_data()
random.shuffle(dummy_data)
data = dummy_data[:7]

"""
print(service.Combinations().pair(data)) # 7♣7♣6♦5♦K♣A♥Q♠
print(service.Combinations().two_pair(data)) # 7♣7♣5♦5♦K♣A♥Q♠
print(service.Combinations().set(data)) # 7♣7♣7♣5♦K♣A♥Q♠
print(service.Combinations().full_house(data)) # 7♣7♣7♣5♦5♦K♣A♥
print(service.Combinations().carey(data)) # 7♣7♣7♣7♣5♦K♣A♥
service.Combinations().straight("A♣2♠4♦5♥3♠6♠7♠")  # A♣2♠4♦5♥3♠6♠7♠
service.Combinations().flush('7♣7♣7♣7♣5♦K♣A♥')"""
service.Combinations().straight_flush("A♣2♠4♠5♠3♠6♠7♣")