class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
    def __str__(self):
        return f"{self.suit} {self.value}"

class Hand:
    def __init__(self):
        self.cards = []
    
    def draw(self, deck):
        self.cards.append(deck.draw())

class Deck:
    def __init__(self)