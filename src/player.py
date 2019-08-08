# Write a class to hold player information, e.g. what room they are in
# currently.

# YOUR CODE GOES HERE!

class Player():
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room

    def __str__(self):
        return f"Hello {self.name} you are in room {self.current_room.name}."
