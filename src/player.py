from room import Room

# Write a class to hold player information, e.g. what room they are in
# currently.


class Player():
    def __init__(self, name, room):
        self.name = name
        self.room = room

    # def move(self, direction):
    #     if self.room.connect[direction] is not None:
    #         self.room = self.room.connect[direction]
    #     else:
    #         print("You can't go that way")
