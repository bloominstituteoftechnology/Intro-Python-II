# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.items = []

    def grab_item(self, item):
        self.current_room.delete_item(item)
        self.items.append(item)
        return f"Great find! You grabbed {item.name}"

    def __str__(self):
        return f"{self.name}"