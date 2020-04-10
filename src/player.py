# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, current_room, name = "Player 1"):
        self.name = name
        self.current_room = current_room
        self.inventory = []

    def update_room(self, room):
        self.current_room = room
    
    def get_inventory(self):
        print("Inventory:")
        for item in self.inventory:
            print(item.name, item.description)

