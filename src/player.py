# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, room, items=[]):
        self.room = room
        self.items = items

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def get_all_items(self):
        if len(self.items) == 0:
            return "none"

        items_str = ""
        for item in self.items:
            items_str = items_str + " " + item
        return items_str