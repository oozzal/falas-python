class Card:
    def __init__(self, suit: str, rank: tuple):
        self.suit = suit
        self.rank = rank

    def value(self) -> int:
        return self.rank[1]

    # so that print by class works
    def __repr__(self) -> str:
        return f" {self.rank[0]}{self.suit} "

    # so that cards.sort() works
    def __lt__(self, other) -> bool:
        return self.value() < other.value()
