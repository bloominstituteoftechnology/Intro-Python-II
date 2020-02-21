# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, current_room, items=[]):
        self.name = name
        self.current_room = current_room
        self.items = items

    def __str__(self):
        return f"{self.name}\n{self.current_room}"

    def take_item(self, item):
        self.items.append(item)
        return f"You take the {item}"

    def drop_item(self, item):
        self.items.remove(item)
        return f"You dropped {item}"