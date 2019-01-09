# Write a class to hold player information, e.g. what room they are in
# currently.
from room import Room
class Player:
    def __init__(self, name, current_room, inventory):
        self.name = name
        self.current_room = current_room
        self.inventory = inventory
        self.maxhealth = 100
        self.health = self.maxhealth
        self.attack = 10
    def __repr__(self):
        return "<Player | Name: {} | Location: {} | Inventory: {} ".format(self.name, self.current_room, self.inventory)