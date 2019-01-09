# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, items=[]):
        self.name = name
        self.description = description
        self.items = items

    def add_item(self, item):
        self.items.append(item)

    def get_all_items(self):
        items_str = ""
        for item in self.items:
            items_str + " " + item
        return items_str