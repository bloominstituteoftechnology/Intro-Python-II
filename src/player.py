# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, playerName, race, vocation, level, experiencePoints, currentRoom):
        self.playerName = playerName
        self.race = race
        self.vocation = vocation
        self.level = level
        self.experiencePoints = experiencePoints
        self.currentRoom = currentRoom

    def __repr__(self):
        return f'<{self.playerName}, you are in the {currentRoom}>'


player1 = Player("Aragorn", "Dunedain", "Ranger", 10, 100, {currentRoom})
print(player1)