# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, name, description, items = [], item_locations = None):
        self.name = name
        self.description = description
        self.n_to = None
        self.e_to = None
        self.s_to = None
        self.w_to = None
        self.items = items
        self.item_locations = item_locations

    def __str__(self):
        output = f'Room: {self.name} \n'
        output += f'Description: {self.description}'
        return output

    def look_around_room(self):
        print(self.item_locations)

    def prnt_items(self):
        for item in self.items:
            print(item)

    def player_took_items(self):
        self.items = []

