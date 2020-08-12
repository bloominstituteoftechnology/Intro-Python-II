# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, currentRoom):
        self.name = name
        self.currentRoom = currentRoom

    def __str__(self):
        return f"{self.name}\n\n {self.currentRoom}"

    def move(self, direction):
        next_room = getattr(self.currentRoom, f"{direction}_to")
        if next_room != None:
            self.currentRoom = next_room
        else:
            print("Not Allowed to go that way")
