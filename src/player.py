# Write a class to hold player information, e.g. what room they are in
# currently.


class Player():
    def __init__(self, room):
        self.room = room

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)

    def __repr__(self):
        return str(self.__class__) + ": " + str(self.__dict__)
