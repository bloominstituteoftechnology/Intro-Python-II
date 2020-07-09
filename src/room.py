# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def n_to(self):
        return Room

    def s_to(self):
        return self.name

    def e_to(self):
        return self.name

    def w_to(self):
        return self.name