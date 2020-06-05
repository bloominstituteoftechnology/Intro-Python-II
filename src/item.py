class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f' {self.name}, {self.current_room}'

class Sword(Item):
    def __init__(self):
        super().__init__(name = "Sword", description = "The Ultimate Treasure")