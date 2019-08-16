# Write a class to hold player information, e.g. what room they are in
# currently.
from room import Room

class Player():
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room

    # output = self.name + " is in room " + self.current_room
    # print(output)

    def __str__(self):
    #     output = ""
        return self.name + " is in room " + self.current_room
        # return  output



