from hand import Hand
from deck import Deck


class Game:
    def __init__(self, num_players=3):
        if num_players > 17:
            raise ValueError("Too many players for a single deck")
        self.num_players = num_players
        self.deck = Deck()
        self.hands = []

    def start(self):
        self.deck.shuffle()
        for _ in range(self.num_players):
            cards = []
            for _ in range(3):
                cards.append(self.deck.deal())
            self.hands.append(Hand(cards))

    def display(self):
        for hand in self.hands:
            hand.display()

    def show(self, i=0) -> Hand:
        winner = self.hands[i]
        for challenger in self.hands:
            if winner == challenger:
                continue
            if not winner > challenger:
                winner = challenger
        return winner
