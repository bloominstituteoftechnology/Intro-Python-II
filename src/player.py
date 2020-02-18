# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, player_name, current_room):
        self.player_name = player_name
        self.current_room = current_room

    def movement(self, cardinal):
        next_room = getattr(self.current_room, f'{cardinal}_to')
        if next_room is not None:
            self.current_room = next_room
            print(self.current_room)

    def __str__(self):
        return f'hello, {self.player_name} you are currently in {self.current_room}'
