# Implement a class to hold room information. This should have name and
# description attributes.

class Room():
    def __init__(self, name, description, items=[], **kwargs):
        self.name = name
        self.description = description
        self.items = items
        self.n_to=None
        self.s_to=None
        self.e_to=None
        self.w_to=None

    def move_further(self, direction):
        directions = {'n': self.n_to, 's': self.s_to, 'e': self.e_to, 'w': self.w_to}
        new_room = directions[direction]
        if direction in directions.keys() and new_room is not None:
            print('You have moved', direction)
            return new_room
        else:
            return "\nThere is no way forward in that direction from where you are."        
