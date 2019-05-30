# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, startingRoom):
        self.name = name
        self.currentRoom = startingRoom

    def travel(self, direction):
        nextRoom = self.currentRoom.getRoomInDirection(direction)
        if nextRoom is not None:
            self.currentRoom = nextRoom
            print(self.currentRoom)
        else:
            print("You cannot move in that direction.")
