# Write a class to hold player information, e.g. what room they are in
# currently.

class Player: 
    def __init__(self, name, room):
        self.name = name 
        self.room = room 
    
    def move(self, direction): 
        if direction in ['n', 's', 'e', 'w']: 
            next_room = self.room.get_direction(direction)
            if next_room is not None:
                self.room = next_room
                print(self.room)
            else: 
                print("Oops! Can't move in that direction.")