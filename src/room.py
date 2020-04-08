# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, n_to=None, s_to=None, e_to=None, w_to=None):
        self.name = name
        self.description = description

        if n_to is None:
            self.n_to = []
        else:
            self.n_to = n_to

        if s_to is None:
            self.s_to = []
        else:
            self.s_to = s_to

        if e_to is None:
            self.e_to = []
        else:
            self.e_to = e_to

        if w_to is None:
            self.w_to = []
        else:
            self.w_to = w_to