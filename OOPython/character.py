import random


class Thief:
    sneaky = True

    @staticmethod
    def pickpocket(self):
        if self.sneaky:
            return bool(random.randint(0, 1))
        return 'You aren\'t sneaky!'


rob = Thief()
print(Thief.pickpocket(rob))
