# Write a class to hold player information, e.g. what room they are in
# currently.
#assigned name and room properties as well as method to return name and location.
class Player:
    def __init__(self, name, room):
        self.name = name
        self.room = room

    def __str__(self):
        return f'{self.name}, is in {self.room}'
        