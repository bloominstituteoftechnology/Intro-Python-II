# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, race, vocation, level, experience_points, location):
        self.name = name
        self.race = race
        self.vocation = vocation
        self.level = level
        self.experience_points = experience_points
        self.location = location


player1 = Player("Aragorn", "Dunedain", "Ranger", 10, 100, )
print(player1)