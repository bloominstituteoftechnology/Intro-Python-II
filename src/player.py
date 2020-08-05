# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, current_room, light_source_on: bool = True):
        self.name = name
        self.current_room = current_room
        self.light_source_on = light_source_on

    def __str__(self):
        return f'{self.name}, your adventure continues.\n \nLocation: {self.current_room.name}.\n \nWhat will you do?'