# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.inventory = []

    def __repr__(self):
        return f'{self.name} is currently in the {self.current_room} and holds the following items: {self.inventory}. '

    def move(self, attribute):
        if hasattr(self.current_room, attribute):
            self.current_room = getattr(self.current_room, attribute)
        else:
            print("That way is inaccessible, please go a different direction.\n")

    def take_item(self, item):
        self.inventory.append(item)

    def drop_item(self, item):
        self.inventory.remove(item)
