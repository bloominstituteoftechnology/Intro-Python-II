# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, n_to=0, s_to=0, e_to=0, w_to=0):
        self.name = name
        self.description = description
        self.n_to = n_to
        self.s_to = s_to
        self.w_to = w_to
        self.e_to = e_to
        self.items = list

    def addItem(self, item):
        self.items.append(item)

    def __str__(self):
        return f''