# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, room, name ):
        self.name = name
        self.room = room
        self.inventory = []
    # def move(self, current_room):
    #     self.current_room = current_room
    #     direction = ['n', 's', 'e', 'w']
    #     if current_room = direction[0]
    #     return 