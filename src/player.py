# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room, inventory=[]):
        self.name = name
        self.current_room = current_room
        self.inventory = inventory
    def __str__(self):
        return (f"{self.name} is in the {self.current_room}.")

    def travel(self, direction):
        if hasattr(self.current_room, f'{direction}_to'):
            current_room =getattr(self.current_room, f'{direction}_to')
            self.current_room = current_room
            print(f"You have entered the {current_room}.\n")
            print(current_room.description + "\n")
        else:
            print("Wrong way!\n")
    def add_item(self, item):
        self.inventory.append(item)
        print(f'{item} is yours now!')
    def item_inventory(self):
        if len(self.inventory) == 0:
            print('You have no items in your inventory')
        else:
            print("Your Inventory")
            for item in self.inventory:
                print(f'{item.name} {item.description} ')