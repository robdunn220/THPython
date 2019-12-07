from OOPython.DiceRoll.dice import Dice


class Hand(list):
    def __init__(self, size=0, die_class=None, *args, **kwargs):
        if not die_class:
            raise ValueError('You must provide dice')
        super().__init__()

        for _ in range(size):
            self.append(die_class(size))
        self.sort()

    def _by_value(self):
        die = {1: [], 2: [], 3: [], 4: [], 5: [], 6: []}
        for dice in self:
            die[int(dice)].append(dice)
        return die


class YahtzeeHand(Hand):
    def __init__(self, *args, **kwargs):
        super().__init__(size=5, die_class=Dice, *args, **kwargs)


# hand = YahtzeeHand()
# hand2 = Hand(6, Dice)
# print(hand._by_value())
