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
        return f'{self.name} {self.description}' 

    def add_items(self, room_item):
        self.items.append(room_item)

    def show_items(self):
        for item in self.items:
            return f"There is an item in the room. {item.name}: {item.description}"