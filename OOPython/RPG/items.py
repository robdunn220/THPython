from OOPython.RPG.inventory import Inventory


class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return '{}: {}'.format(self.name, self.description)


class Weapon(Item):
    def __init__(self, name, description, power):
        super().__init__(name, description)
        self.power = power


wand = Weapon('Wand', 'A magical wand that allows the wielder to cast spells', 6)
dagger = Weapon('Dagger', 'A small, pointed blade. Easily concealed, it is often used in covert situations', 4)

robs_inventory = Inventory()

robs_inventory.add(wand)
robs_inventory.add(dagger)

print(robs_inventory.__iter__())
