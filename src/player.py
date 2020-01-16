# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.items = []

    def move(self, direction):
        next_room = self.current_room.get_room_in_direction(direction)
        if next_room is not None:
            self.current_room = next_room
            print(f"~~~~~~~~~~You moved to {self.current_room.name}~~~~~~~~~~")
        else:
            print("~~~~~~~~~~There is no room in that direction. Please choose another direction.~~~~~~~~~~")

    def get_item(self, item):
        self.items.append(item)

    def drop_item(self, item):
        self.items.remove(item)            
