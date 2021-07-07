# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, currentRoom, playerName, playerItem = []):
        self.currentRoom = currentRoom
        self.playerName = playerName
        self.playerItem = playerItem

    def __str__(self):
        return f"{self.playerName} is currently in room: {self.currentRoom}"