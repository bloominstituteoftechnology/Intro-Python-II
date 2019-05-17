class Item:
    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price

    def __str__(self): #string representation for end users to be able to see
        return self.name + "\t" + self.description + "\t$" + str(self.price)

i = Item("sword", "A sharp item", 3)
print(i)