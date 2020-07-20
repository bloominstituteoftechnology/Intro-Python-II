# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.inventory = []

    def move(self, direction):
        if hasattr(self.current_room, direction):
            self.current_room = getattr(self.current_room, direction)
        else:
            print("You cannot move in that direction")

    def take_item(self, item_to_get):
        for room_item in self.current_room.items:
            if room_item == item_to_get:
                self.current_room.items.remove(room_item)
                self.inventory.append(room_item)
                room_item.on_take()

    def drop_item(self, item_to_drop):
        for player_item in self.inventory:
            if player_item == item_to_drop:
                self.inventory.remove(player_item)
                self.current_room.items.append(player_item)
                player_item.on_drop()

    def get_inventory(self):
        if len(self.inventory) > 0:
            inventory_output = "You currently carry"
            for i, item in enumerate(self.inventory):
                inventory_output += " " + str(i+1) + "." + item
            return print(inventory_output)
        else:
            return print("You don't have anything in the inventory.")