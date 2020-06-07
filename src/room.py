# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, n_to=None, e_to=None,
     s_to=None, w_to=None):
        self.name = name
        self.description = description
        self.inventory = []
        self.connections = dict()
        self.connections['n'] = n_to
        self.connections['e'] = e_to
        self.connections['s']= s_to
        self.connections['w'] = w_to   