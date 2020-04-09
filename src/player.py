from colors import print_color
# Write a class to hold player information, e.g. what room they are in
# currently.


class Player():
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room

    directions = {
        'n': 'North',
        's': 'South',
        'e': 'East',
        'w': 'West'
    }

    def move(self, direction):
        try:
            room = getattr(self.current_room, f'{direction}_to')
            self.current_room = room
        except:
            print_color('red',
                        f'\n\n\nThere is no room to the {self.directions[direction]} of this room.\n\n')
