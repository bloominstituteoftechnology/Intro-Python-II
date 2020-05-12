from room import Room

# Write a class to hold player information, e.g. what room they are in
# currently.

class Player():
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room

    def room_info(self):
        name = self.current_room.name
        description = self.current_room.description
        return f'{name} - {description}'
