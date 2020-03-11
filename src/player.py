# Write a class to hold player information, e.g. what room they are in
# currently.


class Player():
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room

    def move(self, direction):
        room_entered = getattr(self.current_room, f'{direction}_to')
        if room_entered is None:
            print("You can't go that way!")
        elif room_entered is not None:
            self.current_room = room_entered
            print('Your location: ', self.current_room.name)
            print(self.current_room.description)