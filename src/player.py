# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room, inventory):
        self.name = name
        self.current_room = current_room
        self.inventory = inventory
    def travel(self, direction):
        if getattr(self.current_room, f"{direction}_to") is not None:
            self.current_room = getattr(self.current_room, f"{direction}_to")
            print(self.current_room)
        else:
            print("There is no room there.")
    def drop_item(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            print(f"{item} dropped.")
            return True
        else:
            print("You don't have that item.")
            return False
    def pickup_item(self, item):
        self.inventory.append(item)
        print(f"{item} added to inventory.")
    def show_inventory(self):
        for i in self.inventory:
            print(i.name)