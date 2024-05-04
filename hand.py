from enum import Enum


class Result(Enum):
    BADI = 1
    JOOT = 2
    COLOR = 3
    RUN = 4
    DOUBLE_RUN = 5
    TRIAL = 6


class Hand:
    def __init__(self, cards):
        self.cards = cards
        self.cards.sort()
        self.result = self.identify()

    def identify(self) -> Result:
        result = Result.BADI
        ranks = list(set([card.value() for card in self.cards]))
        ranks.sort()
        if len(ranks) == 1:
            return Result.TRIAL
        if len(ranks) == 2:
            return Result.JOOT

        suits = list(set([card.suit for card in self.cards]))
        if len(suits) == 1:
            result = Result.COLOR

        if ranks[2] - ranks[0] == 2 or ranks[2] - ranks[1] == 11:
            if result == Result.COLOR:
                return Result.DOUBLE_RUN
            else:
                return Result.RUN

        return result

    # winner > challenger
    def __gt__(self, other) -> bool:
        if self.result.value > other.result.value:
            return True
        if self.result.value < other.result.value:
            return False

        for i in range(2, -1, -1):
            if self.cards[i] > other.cards[i]:
                return True
            if self.cards[i] < other.cards[i]:
                return False
        return False

    def display(self):
        print(self.cards, "=>", self.result.name)
