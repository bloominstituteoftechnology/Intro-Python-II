# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room

    def __str__(self):
        return f'name: {self.name}, room:{self.current_room}'

    def move(self, direction):
        nextRoom = self.current_room.get_room(direction)
        if nextRoom is not None:
            self.current_room = nextRoom
            print(self.current_room)
        else:
            print("Cannot go that way choose another")

# new_player = Player("Dan", "outside")

# print(new_player)