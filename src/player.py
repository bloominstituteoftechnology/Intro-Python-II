# Write a class to hold player information, e.g. what room they are in
# currently.

#reserved for future use
class Mob:
    def __init__(self, name, health, experience):
        self.name = name
        self.health = health
        self.experience = experience
        
class Player(Mob):
    def __init__(self, name, health, experience = 0, gold = 0):
        super().__init__(name, health, experience)        
        self.gold = gold
        self.inventory = []

    def __str__(self):
        return f"{self.name} has {self.health} health, {self.gold} gold, and {self.experience} experience"

class Monster(Mob):
    def __init__(self, name, health, experience):
        super().__init__(name, health, experience)        

    def __str__(self):
        return f"{self.name} has {self.health} health and is worth {self.experience} experience"