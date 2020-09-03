# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room

    def __str__(self):
        return f"You are in the {self.current_room.name}. \n {self.current_room.description}" 

    def travel(self, direction):
        try:
            self.current_room = getattr(self.current_room, f'{direction}_to')

        except AttributeError:
            print('\n', end='')
            print(f'There is no path in that direction, {self.name}.')
            print('\n', end='')