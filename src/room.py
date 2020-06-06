# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.items = []
    def __str__(self):
        room_items = f'{self.name} {self.description} Items: {self.items}'
        for i in self.items:
            room_items += f'{i}'
        return room_items
    