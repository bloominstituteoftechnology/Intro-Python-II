# Implement a class to hold room information. This should have name and
# description attributes.

class Room():
    def __init__(self, name, description, n_to='wall', s_to='wall', 
                 e_to='wall', w_to='wall'):
        self.name = name
        self.description = description
        self.stuff = []
        self.n_to = n_to
        self.s_to = s_to
        self.e_to = e_to
        self.w_to = w_to

    def add_stuff(self, item):
        self.stuff.append(item)

    def drop_stuff(self, item):
        self.stuff.remove(item)
