# Write a class to hold player information, e.g. what room they are in
# currently.

from room import Room
class Player:
    def __init__(self, name="", currentRoom=Room()):
        self.name = name
        self.currentRoom = currentRoom

    def __str__(self):
        return "Player name: {}, in room: {}".format(self.name, self.currentRoom.name)