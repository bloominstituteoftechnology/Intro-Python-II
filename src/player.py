# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:

    def __init__(self, name, room):
        self.name = name
        self.room = room
        self.items = []

    def print_items(self):
        if not self.items:
            pass
        else:
            for i in self.items:
                print(i.name)