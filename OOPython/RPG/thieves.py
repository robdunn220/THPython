import random
from OOPython.RPG.character import Character
from OOPython.RPG.attributes import Sneaky, Agile


class Thief(Character, Sneaky, Agile):
    @staticmethod
    def pickpocket(self):
        if self.sneaky:
            return self.sneaky and bool(random.randint(0, 1))
        return 'You aren\'t sneaky!'
