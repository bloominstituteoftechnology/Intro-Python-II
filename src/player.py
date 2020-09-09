# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room

    def __str__(self):
        return f"{self.name} is in {self.current_room}"

    def move(self, direction):
        if direction == 'n':
            print("You moved north")
        elif direction == 's':
            print("You moved south")
        elif direction == 'w':
            print("You moved west")
        elif direction == 'e':
            print("You moved east")
        else:
            print("You didn't enter a proper direction. i.e 'n', 's', 'e', 'w' ")