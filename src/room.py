# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, n_too=0, s_too=0, e_too=0, w_too=0):
        self.name = name
        self.description = description
        self.n_too = n_too
        self.s_too = s_too
        self.w_too = w_too
        self.e_too = e_too
    def __str__(self):
        return 