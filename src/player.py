# Write a class to hold player information, e.g. what room they are in
# currently.
from item import Item


class Player:
    def __init__(self, name, starting_room):
        self.name = name
        self.current_room = starting_room
        self.items = []

    def travel(self, direction):
        # Check if there's a valid room in the direction
        if getattr(self.current_room, f"{direction}_to") is not None:
            # If so, update current_room to new room and print description
            self.current_room = getattr(self.current_room, f"{direction}_to")
            print(self.current_room)
        else:
            # Else print an error message
            print("Sorry! there's no room here.", "\n")

    def _get_item_string(self):
        return ", ".join([item.name for item in self.items])

    def print_inventory(self):
        if len(self.items) > 0:
            return "You are carrying: \n" + ", ".join([item.name for item in self.items])
        else:
            return ""
