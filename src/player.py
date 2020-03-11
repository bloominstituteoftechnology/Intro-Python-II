# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, current_room):
        self.current_room = current_room

    def __repr__(self):
        return 'Current Location: {}'.format(self.current_room)
