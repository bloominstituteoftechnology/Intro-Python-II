# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
    
    def __str__(self):
        return f'''
            name: {self.name}\n
            desc: {self.desc}\n
            n_to: {self.n_to}\n
            s_to: {self.s_to}\n
            e_to: {self.e_to}\n
            w_to: {self.w_to}\n'''