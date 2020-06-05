# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description

        self.n_to: Room = None
        self.s_to: Room = None
        self.e_to: Room = None
        self.w_to: Room = None

    def __str__(self):
        result = 'You are at {self.name}. {self.description}\n'.format(self=self)
        return result
