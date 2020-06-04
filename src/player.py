# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, room):
        self.name = name
        self.room = room

    def __str__(self):
        return f"\nNow you are in the {self.room.name}. {self.room.description}."

    def move(self, direction):
        if getattr(self.room, f"{direction}_to") is not None:
            self.room = getattr(self.room, f"{direction}_to")
            print(self)
        else:
            print("\nTry a different direction")