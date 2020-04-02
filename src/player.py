# Write a class to hold player information, e.g. what room they are in
# currently.
from room import Room

class Player:
    def __init__(self, current_room, items=[]):
        self.current_room = current_room
        self.items = items

    def try_north(self):
        if self.current_room.n_to != None:
            self.current_room = self.current_room.n_to
        else:
            print("**You can't go north from this room. Please enter a different direction.**")

    def try_south(self):
        if self.current_room.s_to != None:
            self.current_room = self.current_room.s_to
        else:
            print("**You can't go south from this room. Please enter a different direction.**")

    def try_east(self):
        if self.current_room.e_to != None:
            self.current_room = self.current_room.e_to
        else:
            print("**You can't go east from this room. Please enter a different direction.**")

    def try_west(self):
        if self.current_room.w_to != None:
            self.current_room = self.current_room.w_to
        else:
            print("**You can't go west from this room. Please enter a different direction.**")

    def get_item(self, item):
        if item in self.current_room.items:
            self.current_room.items.remove(item)
            self.items.append(item)
            item.on_take()
        else:
            print(f"There is no {item.name.lower()}")

    def drop_item(self, item):
        if item in self.items:
            self.items.remove(item)
            self.current_room.items.append(item)
            item.on_drop()
        else:
            print(f"{item.name} is not in your inventory.")

    def print_items(self):
        if len(self.items) > 0:
            item_list = "You are holding the following items:"
            for item in self.items:
                item_list += f"\n\t-{item}"
        else:
            item_list = "You are not holding anything"
        print(item_list)