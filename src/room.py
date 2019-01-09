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
        items_str = "Items: "

        if len(self.items) == 0:
            return items_str + "none"

        items_str = "Items:"
        for item in self.items:
            items_str = items_str + " " + item
        return items_str