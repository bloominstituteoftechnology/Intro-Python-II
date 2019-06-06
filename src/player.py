# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:

    def __init__(self, name, room):
        self.name = name
        self.room = room
    
    def __str__(self):
        return f'{self.name} is in {self.room}'

    def get_name(self):
        return str(self.name)
    def get_current_room(self):
        return str(self.current_room)