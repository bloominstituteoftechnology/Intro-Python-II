# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.list_items = []

    def get_item(self, item):
        self.list_items.append(item)

    def remove_item(self, item):
        self.list_items.remove(item)
