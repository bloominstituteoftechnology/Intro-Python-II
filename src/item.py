class Item:
    def __init__(self, name, description, quantity):
        self.name = name
        self.description = description
        self.quantity = quantity
    def __repr__(self):
        return(f'{self.name}, {self.description}')