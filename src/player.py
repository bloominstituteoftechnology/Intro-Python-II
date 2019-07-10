# Write a class to hold player information, e.g. what room they are in
# currently.
from room import Room

class Player:
    health = 100
    inventory = []
    movement_speed = 100

    def __init__(self, name, description, currentRoom):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.currentRoom = currentRoom

    def pickup_item(self, item):
        self.inventory.append(item)

    def try_move(self, direction):
        pass
# https://www.youtube.com/watch?v=1L1Ta87SOqc&feature=youtu.be 1:33