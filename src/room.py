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
        return f'Location: {self.name} \n \n Hint: {self.description} \n Items in this locations: {self.items_in_room}.'

    def add_room_item(self, item):
        self.items_in_room.append(item)
