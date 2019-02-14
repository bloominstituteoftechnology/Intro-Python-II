# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, currentRoom, playerName):
        self.currentRoom = currentRoom
        self.playerName = playerName

    def __str__(self):
        return f"{self.playerName} is currently in room: {self.currentRoom}"