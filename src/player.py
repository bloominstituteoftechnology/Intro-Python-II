# Write a class to hold player information, e.g. what room they are in
# currently.

from room import Room


class Player:

    def __init__(self, name, current_room, items=None):
        self.name = name
        self.current_room = current_room
        self.items = [] if items is None else items

    def print_items(self):
        if len(self.current_room.items) > 0:
            for i in self.items:
                print(i)

        else:
            print('no items for you in this room')
