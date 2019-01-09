# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, items=[], is_light=True):
        self.name = name
        self.description = description
        self.items = items
        self.is_light = is_light

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def get_all_items(self):
        items_str = "Items: "

        if len(self.items) == 0:
            return items_str + "none"

        for item in self.items:
            items_str = items_str + " " + item
        return items_str