
class Item:
        def __init__(self, name, t, durability):
            self.name = name
            self.type = t
            self.durability = durability

        def __str__(self):
            return f'Item Name: {self.name}'
