# Write a class to hold player information, e.g. what room they are in
# currently.

#reserved for future use
class Mob:
    def __init__(self, name, health, experience):
        self.name = name
        self.health = health
        self.experience = experience
        
class Player(Mob):
    def __init__(self, name, health, experience, gold):
        super().__init__(name, health, experience)        
        self.gold = gold

    def __str__(self):
        return "{} has {} health, {} gold, and {} experience".format(
            self.name,
            self.health,
            self.gold,
            self.experience
        )

class Monster(Mob):
    def __init__(self, name, health, experience):
        super().__init__(name, health, experience)        

    def __str__(self):
        return "{} has {} health and is worth {} experience".format(
            self.name,
            self.health,
            self.experience
        )