class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self._shares = shares
        self.price = price

    def __repr__(self):
        return f'Stock(\'{self.name}\', {self._shares}, {self.price}'

    @property
    def cost(self):
        print(self._shares * self.price)

    def sell(self, amount):
        if amount > self._shares:
            print('Error: Amount is greater than available shares:', self._shares)
            return
        self._shares -= amount

    @property
    def shares(self):
        return self._shares

    @shares.setter
    def shares(self, value):
        if not isinstance(value, int):
            raise TypeError('Expected int')
        self._shares = value
    

class MyStock(Stock):

    def __init__(self, name, shares, price, factor):
        super().__init__(name, shares, price)
        self.factor = factor

    def panic(self):
        self.sell(self._shares)

    def cost(self):
        actual_cost = super().cost()
        return self.factor * actual_cost
