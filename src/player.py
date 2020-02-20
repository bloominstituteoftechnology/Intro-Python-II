# Write a class to hold player information, e.g. what room they are in
# currently.

from room import Room
class Player:
    def __init__(self, name="", current_room=Room(), items=[]):
        self.name = name
        self.current_room = current_room
        self.items = items

    def __str__(self):
        return "Player name: {}, in room: {}".format(self.name, self.current_room.name)