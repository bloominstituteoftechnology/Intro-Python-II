from gameObj import GameObj

class Room(GameObj):
    def __init__(self, name, desc, holding=[]):
        super().__init__(name, desc, holding)
        self.n_to = None
        self.e_to = None
        self.s_to = None
        self.w_to = None
        self.u_to = None
        self.d_to = None

    def __str__(self):
        return f'{self.desc}\n'