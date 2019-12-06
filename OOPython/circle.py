class Circle:
    def __init__(self, diameter):
        self.diameter = diameter

    @property
    def radius(self):
        return self.diameter / 2

    @radius.setter
    def radius(self, radius):
        self.diameter = radius * 2


class Product:
    _price = 0.0
    tax_rate = 0.12

    def __init__(self, base_price):
        self._price = base_price

    @property
    def price(self):
        return self._price + (self._price * self.tax_rate)

    @price.setter
    def price(self, price):
        self._price = price


p = Product(5)
p.price = 10

print(p.price)
