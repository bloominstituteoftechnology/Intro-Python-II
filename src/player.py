# Write a class to hold player information, e.g. what room they are in
# currently.
class Player():
    def __init__(self, name, current_room):
        self.name = name 
        self.current_room = current_room

    def move(self, direction):
        new_room = getattr(self.current_room, f'{direction}_to')
        if new_room == None:
            print("Please choose a different direction")
        elif new_room is not None: 
            self.current_room = new_room
            print("Your current location is:", self.current_room.name)
            print(self.current_room.description)
    def show_room(self):
            print(self.current_room.description)

