# Write a class to hold player information, e.g. what room they are in
# currently.

class Player():

    def __init__(self, name, current_room):
        self.name = name
        self.__current_room = current_room

    def get_current_room(self):
        return self.__current_room

    def set_current_room(self, room):
        if room != None:
            self.__current_room = room
        else:
            self.__current_room = self.__current_room

    current_room = property(get_current_room, set_current_room)