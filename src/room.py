# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.s_to = ""
        self.n_to = ""
        self.w_to = ""
        self.e_to = ""
        self.item_list = []

