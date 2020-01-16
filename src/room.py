# Implement a class to hold room information. This should have name and
# description attributes.
class Room:

    def __init__(self, name, description, items):
        self.name = name
        self.description = description
        self.items = items
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None

    def __str__(self):
        if len(self.items) == 2:
            return f'Name~> {self.name}\nDescription~> {self.description}\nItems~> {self.items[0]} and {self.items[1]}'
        elif len(self.items) == 1:
            return f'Name~> {self.name}\nDescription~> {self.description}\nItems~> {self.items[0]}'
        else:
            return f'Name~> {self.name}\nDescription~> {self.description}\nItems~> None'

    def get_room_in_direction(self, direction):
        if hasattr(self, f"{direction}_to"):
            return getattr(self, f"{direction}_to")
        return None

    def remove_item(self, item):
        self.items.remove(item)