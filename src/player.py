# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.player_inventory=[]

    # method to move player from one room to another
    def move_player(self, direction):
        if getattr(self.current_room, f'{direction}_to') != None:
            self.current_room = getattr(self.current_room, f'{direction}_to')
        else:
            print("Invalid move. Please try again.")

    # method to add item found in current room to "player_inventory"
    def get_item(self, item):
        self.player_inventory.append(item)
        print(f"You picked up {item}.")

    # method to remove item from "player_inventory"
    # to then drom in "current_room"
    def drop_item(self, item):
        self.player_inventory.remove(item)
        print(f"You dropped {item}.")


