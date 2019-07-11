# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, good, species, room, items):
        self.name = name
        self.room = room 
        self.items = []
        self.isGood = good
        self.health = 100
        self.money = 100
        self.species = species

    def locate(self):
        return print(f'{self.room}')

    def __getAge__(self):
        return f'{self.name} is {self.age} years old'
