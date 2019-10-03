# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name= 'Higby', char_class='investigator', location='outside', inventory = []):
        self.name = name
        self.char_class = char_class
        self.location = location
        self.inventory = inventory
    
    def move_location(self, movement):
        self.location = movement

    def add_item(self, item):
        self.inventory.append(item)
    def drop_item(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
        else:
            "But you don't have one of those!"

    def __str__(self):
        return f'You are {self.name}, a foolish young {self.char_class} who is currently standing at the {self.location} of the cavern'
    def __repr__(self):
        return f'Player({repr(self.name)},{repr(self.char_class)},{repr(self.location)},{repr(self.inventory)})'

#testPlayer = Player('Test', 'haberdasher', 'outside')
#print(testPlayer)
#print(repr(testPlayer))