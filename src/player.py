# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room

    def move(self, direction):
        new_room = getattr(self.current_room, f"{direction}_to")
        if (new_room) is not None:
            self.current_room = new_room
        else:
            print("Sorry you can't move in that direction")

    def __str__(self):
        return '{self.name} {self.room}'.format(self=self)

    

