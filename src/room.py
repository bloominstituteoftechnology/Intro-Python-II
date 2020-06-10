# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    # Room contains: name, description, items_in_room. Methods: add_item
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.items_in_room = []
        self.n_to = ''
        self.s_to = ''
        self.e_to = ''
        self.w_to = ''

    def __str__(self):
        return f' Current room: {self.name:s} \n Description: {self.description} \n Items In Room: {self.items_in_room} \n '

    def add_room_item(self, item):
        self.items_in_room.append(item)
