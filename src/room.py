# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.n_to = None
        self.e_to = None
        self.s_to = None
        self.w_to = None
        self.items = {}

    def __str__(self):
        if self.name.startswith('Outside'):
            val = f'You are {self.name}.'
        else:
            val = f'You are in the {self.name}.'
        val += f'\n{self.description}'
        return val

    def add_item(self, name, item):
        self.items[name.lower()] = item

    def remove_item(self, item_name):
        if item_name.lower() in self.items:
            del self.items[item_name.lower()]
