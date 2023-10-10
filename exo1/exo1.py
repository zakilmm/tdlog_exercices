class Item:
    def __init__(self, price, weight):
        self.price = price
        self.weight = weight

# Example of usage:
i = Item(10, 20)
print("Price:", i.price)
print("Weight:", i.weight)