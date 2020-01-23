# Write a class to hold player information, e.g. what room they are in
# currently.

class Player():
    def __init__(self, current_room=None):
        self.current_room = current_room
        self.items = {}

    def look(self):
        print(self.current_room.name)
        print(self.current_room.description, "\n")
        print('In The Room: ', self.scan_items(self.current_room.items))
        print('Inventory: ', self.items.keys())

    def scan_items(self, inventory=None):
        scan_list = []
        if inventory is None:
            inventory = self.items
            
        for key in inventory.keys():
            scan_list.append(inventory[key].name)
        return scan_list

    def move(self, direction):
        if direction in self.current_room.connections.keys():
            self.current_room = self.current_room.connections[direction]
        else:
            print('Cannot go that way!')