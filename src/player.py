# Write a class to hold player information, e.g. what room they are in
# currently.

class Player():
    def __init__(self, current_room):
        self.current_room = current_room

    def look(self):
        print(self.current_room.name)
        print(self.current_room.description)

    def move(self, direction):
        if direction in self.current_room.connections.keys():
            self.current_room = self.current_room.connections[direction]
        else:
            print('Cannot go that way!')