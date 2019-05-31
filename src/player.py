# Write a class to hold player information, e.g. what room they are in
# currently.

from room import Room
from item import Item


class Player():

    def __init__(self, name):
        # Initialize name during creation
        self.name = name

        # Place holder for current room information
        self.current_room = None

        # Place holder for items
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def get_items(self):
        return self.items

    def remove_item(self, index):
        self.items.pop(index)

    def set_current_room(self, room):
        self.current_room = room

    def get_current_room(self):
        return self.current_room

    def move_in_dir(self, direction):
        current_room = self.get_current_room()

        # Check if player can move in direction given
        if direction == 'n' and current_room.n_to:
            self.set_current_room(current_room.n_to)
            return True
        elif direction == 's' and current_room.s_to:
            self.set_current_room(current_room.s_to)
            return True
        elif direction == 'e' and current_room.e_to:
            self.set_current_room(current_room.e_to)
            return True
        elif direction == 'w' and current_room.w_to:
            self.set_current_room(current_room.w_to)
            return True

        return False

    def take_item(self, item_name):
        room = self.get_current_room()

        item_picked = False

        for index, item in enumerate(room.get_items()):
            if item.name == item_name:
                item_picked = True
                self.add_item(item)
                room.remove_item(index)

        return item_picked

    def drop_item(self, item_name):
        room = self.get_current_room()

        item_dropped = False

        for index, item in enumerate(self.get_items()):
            if item.name == item_name:
                item_dropped = True
                room.add_item(item)
                self.remove_item(index)

        return item_dropped

    def print_room_info(self):
        print(self.get_current_room())

    def print_items_info(self):
        player_item_list = self.get_items()
        print(f'\n{len(player_item_list)} available items with you.')

        for item in player_item_list:
            print(item)
