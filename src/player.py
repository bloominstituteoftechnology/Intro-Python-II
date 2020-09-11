# Write a class to hold player information, e.g. what room they are in
# currently.

from room import Room
import textwrap

class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room

    def __str__(self):
        return f"{self.name} is in {self.current_room}"

    def move(self, direction):
        if direction in ['n', 's', 'w', 'e']:
            next_room = self.current_room.get_direction(direction)
            if next_room is not None:
                self.current_room = next_room
                print(f"{self.name} you are currently in {self.current_room}\n")
                wrappedDescription = textwrap.wrap(self.current_room.description)
                for line in wrappedDescription:
                     print(line)
        
                print("*******************************************************************\n")
            else:
                print("There is no room in that direction, try another one.\n")  