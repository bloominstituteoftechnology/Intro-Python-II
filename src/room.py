from textwrap import wrap

class Room:
    def __init__(self, name, desc, holding=[]):
        desc = wrap(desc, 50)
        self.name = name
        self.desc = '\n'.join(desc)
        self.holding = holding
        self.n_to = None
        self.e_to = None
        self.s_to = None
        self.w_to = None
    
    def __str__(self):
        return f">> {self.name} <<\n\f{self.desc}\n"