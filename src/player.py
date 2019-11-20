# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, playerName, currentRoom):
        self.playerName = playerName
        self.currentRoom = currentRoom

    def __str__(self):
        return f'Player Name: {self.playerName} and Current Room: {self.currentRoom}'

    playerName = str
    currentRoom = str