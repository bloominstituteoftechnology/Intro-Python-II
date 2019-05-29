# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(name, description, n_to, s_to, e_to, w_to):
        self.name = name
        self.description = description
        self.n_to = n_to