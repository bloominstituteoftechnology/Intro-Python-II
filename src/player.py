from gameObj import GameObj

class Player(GameObj):
    def __init__(self, name, loc, desc='n/a', holding=[]):
        super().__init__(name, desc, holding)
        self.loc = loc

    def __str__(self):
        return f'++ {self.name} is at the {self.loc.name} ++'
