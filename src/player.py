from src.room import Room
from src.directions import Direction


# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, player_name: str, current_room: Room, move_counter: int = 0):
        self.player_name = player_name
        self.current_room = current_room
        self.move_num = move_counter

    def move(self, direction: Direction):

        new_room = self.current_room.get_nearby_room(direction)

        if new_room is None:
            print(f'The path is blocked to the {direction.value}.')
        else:
            self.current_room = new_room
            print(f'Room: {self.current_room.room_name}, Description: {self.current_room.description}')
