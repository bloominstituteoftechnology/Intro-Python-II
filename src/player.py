# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, room, items, moves):
        self.room = room
        self.items = items
        self.moves = moves

    def __str__(self):
        print('bruh requiem')
