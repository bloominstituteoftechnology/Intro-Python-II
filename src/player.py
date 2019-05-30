# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.inventory = []

        #print current state of player
        # def _str_(self):
        #     print(f'{self.name} is in the {self.current_room} room.\n')
    
    def move_player(self, direction):
        if getattr(self.current_room, f'{direction}_to') != None:
            self.current_room = getattr(self.current_room, f'{direction}_to')
        else:
            print("That move is not valid. Please try again.")

    # add item from room to player's inventory
    def get_item(self, item):
        self.inventory.append(item)
        print(f"You picked up {item}")

    # remove item from player's inventory and drop in room
    def drop_item(self, item):
        self.inventory.remove(item)
        print(f"You dropped {item}")