
'''
Creates a player object that contains a name, and what the current room location is.
'''


class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room

    def _print_current_location(self):
        print(
            f'\n{self.name}, you are currently in {self.current_room.name}.\n{self.current_room.description}')

    def _move(self, direction_input):
        self.current_room = self.current_room.__getattribute__(
            f'{direction_input}_to')

    def __str__(self):
        return f'Your name is: {self.name}\nThe current room you are in: {self.current_room}'

    def __repr__(self):
        return f'Player({self.name}, {self.current_room})'
