# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, room_name, room_description, current_room, next_move, next_room):
        self.room_name = room_name
        self.room_description = room_description
        self.current_room = current_room
        self.next_move = next_move
        self.next_room = next_room
