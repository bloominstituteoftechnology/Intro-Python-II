# Item class
class Item():
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __repr__(self):
        return f"{self.name} \n {self.description}"

    def on_get(self, player):
        player.happiness += 1

    def on_drop(self, player):
        player.happiness -= 2
