# Implement a class to hold room information. This should have name and
# description attributes.

class Room:

    n_to = 0
    e_to = 0
    s_to = 0
    w_to = 0

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.items = []

    def __str__(self):
        return f"{self.name}, {self.description}"

    def add_items(self, items):
        self.items = items

    def has_item(self, item_name):
        for item in self.items:
            if item.name == item_name:
                return item

        print("Item is not in the room")
        return None