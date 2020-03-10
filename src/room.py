# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    """
    room class
    """
    def __init__(self, name, description, items=None):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        if items is None:
            self.items = []
        else:
            self.items = items

    def __repr__(self):
        return "Room('{}', '{}', '{}')".format(self.name, self.description, self.items)

    def __str__(self):
        return (f'{self.name},\n {self.description}')

