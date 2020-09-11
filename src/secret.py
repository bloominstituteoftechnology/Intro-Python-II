from item import Item

class Secret(Item):
    def __init__(self, name, value, difficulty):
        self.name = name
        self.value = value
        self.hidden = True
        self.difficulty = difficulty