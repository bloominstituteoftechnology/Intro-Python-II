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

    @property
    def current_room(self):
        return self.__current_room

    @current_room.setter
    def current_room(self, new_value):
        self.__current_room = new_value
        self.__current_room.printAllItems()
        print(f'You moved to room: {self.__current_room.name}')