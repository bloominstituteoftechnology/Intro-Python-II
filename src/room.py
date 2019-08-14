# Implement a class to hold room information. This should have 
# name and description attributes.

class Room: 
    def __init__(self, name, description):
        # self._name = name
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.w_to = None
        self.e_to = None

    def __str__(self):
        return f'Room name: {self.name}, Room description: {self.description}'

    def room_direction(self, direction):
        if direction == "n":
            return self.n_to
        elif direction == "s":
            return self.s_to
        elif direction == "e":
            return self.e_to
        elif direction == "w":
            return self.w_to
        else:
            return None