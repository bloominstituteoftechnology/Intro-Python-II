# Write a class to hold player information, e.g. what room they are in
# currently.

class Player():

    def __init__(self, name, current_room):
        self.name = name
        self.__inventory = []
        self.__current_room = current_room

    def get(self, item):
        self.__inventory.append(item)

    def drop(self):
        if not self.__inventory:
            print("")

    def get_current_room(self):
        return self.__current_room

    def set_current_room(self, room):
        if room != None:
            self.__current_room = room
        else:
            print("\nThere's nothing in this direction! (Use m to open your map\n")
            self.__current_room = self.__current_room

    current_room = property(get_current_room, set_current_room)