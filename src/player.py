from room import Room

# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
     # Here we are describing our players attributes.
    def __init__(self, currentRoom, health):
        self.currentRoom = currentRoom
        self.health = 100
        self.inventory = []
        self.movement_speed = 10
    # Here we are defining the methods for the Player class

    def pickup_item(self, item):
        self.inventory.append(item)

    # def try_move(self, direction):
