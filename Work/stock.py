class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self):
        print(self.shares * self.price)

    def sell(self, amount):
        if amount > self.shares:
            print('Error: Amount is greater than available shares:', self.shares)
            return
        self.shares -= amount
