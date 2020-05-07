# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, location, health=100, score=0, inventory=['pickaxe', 'map', 'bronze sword', 'compass']):
        self.name = name
        self.location = location
        self.health = health
        self.score = score
        self.inventory = inventory

    # updates the Player's location
    def setLocation(self, location):
        self.location = location

    def __str__(self):
        return f'Name: {self.name} \nLocation: {self.location} \nHealth: {self.health} \nScore: {self.score} \nInventory: {self.inventory}'
