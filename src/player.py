# Write a class to hold player information, e.g. what room they are in
# currently.


class Player():
    def __init__(self, playerName, currentRoom, inventory):
        self.playerName = playerName
        self.health = 100
        self.stamina = 50
        self.stength = 10
        self.currentRoom = currentRoom
        self.inventory = inventory

    def __repr__(self):
        return f'{self.playerName} is in the {self.currentRoom}'
