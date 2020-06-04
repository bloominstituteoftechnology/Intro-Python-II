# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, current_room=rooms['outside']):
        self.name = name
        self.current_room = current_room
    
    def __str__(self):
        return f'{self.name}, you are at the {self.current_room}'

    movement = ""

    def move(self):
        if self.movement == 'N':
            print("Moving North")
            if self.current_room == rooms['outside']:
                rooms['outside'].n_to
            elif self.current_room == rooms['foyer']:
                rooms['foyer'].n_to
            elif self.current_room == rooms['narrow']:
                rooms['narrow'].n_to
            else:
                print("Can't move North, pick another direction.")
        elif self.movement == 'S':
            print("Moving South")
            if self.current_room == rooms['foyer']:
                rooms['foyer'].s_to
            elif self.current_room == rooms['overlook']:
                rooms['overlook'].s_to
            elif self.current_room == rooms['treasure']:
                rooms['treasure'].s_to
            else:
                print("Can't move South, pick another direction.")
        elif self.movement == 'E':
            print("Moving East")
            if self.current_room == rooms['foyer']:
                rooms['foyer'].e_to
            else:
                print("Can't move East, pick another direction.")
        elif self.movement == 'W':
            print("Moving West")
            if self.current_room == rooms['narrow']:
                rooms['narrow'].w_to
            else:
                print("Can't move West, pick another direction.")
        else:
            print("Invalid move.")

    player_items = []