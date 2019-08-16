class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __repr__(self):
        return f"{self.name}"

    def __str__(self):
        return f'name: {self.name}, item:{self.description}'


class Rock(Item):
    def __init__(self, name, description, value):
        super().__init__(name, description)
        self.value = value

    def on_take(self, player):
    player.