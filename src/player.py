# Write a class to hold player information, e.g. what room they are in
# currently.

class Player():
    def __init__(self, room):
        self.room = room

    def __str__(self):
        return """\nCurrent Location: {self.room.name}
                  Room Description: {self.room.description}""".format(self = self)
