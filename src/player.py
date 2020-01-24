# Write a class to hold player information, e.g. what room they are in
# currently.
from room import Room
class Player:
    def __init__(self, name, room=[]):
        self.name = name
        self.rooms = rooms

    def __str__(self):
        
        output = f"Player : {self.name}"
        for r in self.rooms:
            output += f"\n\t{r}"
        return output

    def get_name(self):
        return self.name
    
    def set_name(self, new_name):
        self.name = new_name