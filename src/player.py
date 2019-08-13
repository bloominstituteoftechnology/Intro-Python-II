# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, room="outside"):
        self.room = room

    def __str__(self):
        return 'I am in {self.room}'.format(self=self)
