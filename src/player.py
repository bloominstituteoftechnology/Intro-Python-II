# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, room, name="Player", race="human", gender="male"):
        self.name = name
        self.room = room
        self.race = race
        self.gender = gender
        self.inventory = []

    def addItem(self, item):
        self.inventory.append(item)

    def setRoom(self, room):
        self.room = room
