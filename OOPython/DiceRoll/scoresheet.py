from OOPython.DiceRoll.hands import Hand, YahtzeeHand


class YahtzeeScoreSheet:
    def score_ones(self, hand):
        by_value = hand._by_value()
        return sum(by_value[1])

    def _score_set(self, hand, set_size):
        scores = []
        by_value = hand._by_value()
        for worth, count in by_value.items():
            if len(count) == set_size:
                scores.append(worth*set_size)
        return sum(scores)


hand = YahtzeeHand()
robs_sheet = YahtzeeScoreSheet()
print(robs_sheet._score_set(hand, 3))
