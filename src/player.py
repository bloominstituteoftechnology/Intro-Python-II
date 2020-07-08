# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        # self.bag = []
    def directions(self, direction):
        if direction == "n":
            room_i = 0
        elif direction == "e":
            room_i = 1
        elif direction == "s":
            room_i = 2
        elif direction == "w":
            room_i = 3
        if self.current_room.exits[room_i] == None:
            print("An invisable wall with holographic text appears with the words 'access denied'.")
            return None
        else:
            return self.current_room.exits[room_i]