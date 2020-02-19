class Item:
    def __init__(self, items=[]):
        self.name = items[0]
        self.weight = items[1]

    def __str__(self):
        return f'{self.name} weight: {self.weight}'

    def take(self):
        print(f"You picked up {self.name}")

    def drop(self):
        print(f"You dropped {self.name}")
