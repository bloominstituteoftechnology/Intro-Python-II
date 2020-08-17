# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.items = []
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None

    def __str__(self):
        string = ""
        string += f'You are currently in the: {self.name}\n{self.description}\n Item(s) in room: {self.items}'
        return string

    def get_direction(self, direction):
        if direction == 'n':
            return self.n_to
        if direction == 's':
            return self.s_to
        if direction == 'e':
            return self.e_to
        if direction == 'w':
            return self.w_to
        else:
            return None

    def add_items(self, item): 
        self.items.append(item) 

    def take_item(self, item): 
        if item in self.items: 
            self.items.remove(item) 
