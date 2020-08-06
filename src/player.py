# Write a class to hold player information, e.g. what room they are in
# currently.

import textwrap

class Player:

    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.items = []
        # determines if player can move to a room
        self.new_room = True

    # method to print out players current location
    def location(self):
        if self.new_room == True:
            print(f"You are currently in {self.current_room.name}")
            for des in textwrap.wrap(self.current_room.description):
                print(des)
            for item in self.current_room.items:
                print(item)

    def command(self, command):
        if len(command) == 1:
            self.single_command(command[0])
        elif len(command) == 2:
            self.item_command(command)

    # method to determine which way the player chooses to move
    # and if they can go that way.
    def single_command(self, command):
        self.new_room = False
        if command == 'n' and self.current_room.n_to != 0:
            self.current_room = self.current_room.n_to
            self.new_room = True
        elif command == 'e' and self.current_room.e_to != 0:
            self.current_room = self.current_room.e_to
            self.new_room = True
        elif command == 's'and self.current_room.s_to != 0:
            self.current_room = self.current_room.s_to
            self.new_room = True
        elif command == 'w' and self.current_room.w_to != 0:
            self.current_room = self.current_room.w_to
            self.new_room = True
        elif command == 'i' or command == 'inventory':
            self.print_inventory()
        else:
            print("Can't move in that direction, choose another option (n,e,s,w)")

    def item_command(self, command):
        action = command[0]
        item_name = command[1]
        if action == 'get' or action == 'take':
            item = self.current_room.has_item(item_name)
            if item != None:
                item.on_take()
                self.items.append(item)
                self.current_room.items.remove(item)
        elif action == 'drop':
            item = self.has_item(item_name)
            if item != None:
                item.on_drop()
                self.current_room.items.append(item)
                self.items.remove(item)
        else:
            print("Can't do that action")

    def has_item(self, item_name):
        for item in self.items:
            if item.name == item_name:
                return item

        print("You do not have that item in your inventory")
        return None

    def print_inventory(self):
        print("Inventory:")
        for item in self.items:
            print(item.name)