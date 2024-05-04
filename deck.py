import random
from card import Card

SUITS = ["♠️", "♣️", "❤️️", "♦️"]
RANKS = [
    ("2", 2),
    ("3", 3),
    ("4", 4),
    ("5", 5),
    ("6", 6),
    ("7", 7),
    ("8", 8),
    ("9", 9),
    ("10", 10),
    ("J", 11),
    ("Q", 12),
    ("K", 13),
    ("A", 14),
]


class Deck:
    def __init__(self):
        self.cards = []
        for suit in SUITS:
            for rank in RANKS:
                self.cards.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self) -> Card:
        return self.cards.pop()
