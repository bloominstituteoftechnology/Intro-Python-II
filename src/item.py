class Item:
    def __init__(self, id, name, description, gold):
        self.id = id
        self.name = name
        self.description = description
        self.gold = gold

    def __str__(self):
        return f"{self.name} worth {self.gold} gold"