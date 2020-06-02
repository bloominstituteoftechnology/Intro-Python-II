import sys
from player import Player
from room import Room


INVALID_INPUT_WARNING = "<Invalid input; please try again>"


class Game:
    '''The game'''
    def __init__(self, player: Player, rooms: list(Room)):
        self.player = player
        self.rooms = rooms

    def start(self):
        '''Begin the game'''
        print("\n\n-- ADVENTURE GAME --\n\n\n")

        print("(Enter 'q' at any time to quit.)")
        while True:
            self.__update()

    def __update(self):
        print("\n" + self.player.current_room.name)
        print(self.player.current_room.description)

        txt = input("<Move the player (enter 'n', 's', 'e', or 'w')>: ")
        self.__parse_input(txt)

    def __parse_input(self, txt):
        if txt == 'q':
            sys.exit()
        elif len(txt) == 1:
            self.__parse_move(txt)
        else:
            self.__parse_action(txt)

    def __parse_action(self, txt):
        split_txt = txt.split()
        verb = split_txt.pop(0)

        if verb in ("get", "take"):
            self.__parse_get(split_txt)
        if verb == "drop":
            self.__parse_drop(split_txt)

    def __parse_move(self, txt):
        possible_room = self.player.current_room.get_room_in_direction(txt)
        if possible_room is None:
            print(INVALID_INPUT_WARNING)
        else:
            self.player.current_room = possible_room

    def __parse_get(self, split_txt):
        pass

    def __parse_drop(self, split_txt):
        pass
