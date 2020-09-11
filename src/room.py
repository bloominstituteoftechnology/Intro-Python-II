# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, items: List[Item]=None):
        self.name = name
        self.description = description
        self.items: List[Item] = items

    def get_direction(self, direction):
        if direction == 'n':
            return self.n_to
        elif direction == 's':
            return self.s_to
        elif direction == 'e':
            return self.e_to
        elif direction == 'w':
            return self.w_to

    def add_item(self, item):

    def __repr__(self):
        return f'Room({repr(self.name)})'
