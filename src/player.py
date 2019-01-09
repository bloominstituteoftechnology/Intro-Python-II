# Write a class to hold player information, e.g. what room they are in
# currently.


class Player():
    def __init__(self, playerName, currentRoom):
        self.playerName = playerName
        self.currentRoom = currentRoom

    def __repr__(self):
        return f'{self.playerName} is in the {self.currentRoom}'
