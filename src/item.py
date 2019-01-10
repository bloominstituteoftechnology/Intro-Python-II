from player import Player


class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __repr__(self):
        return self.name

    def on_take(self):
        return f'\nPicked up {self.name}\n{self.description}\n'
