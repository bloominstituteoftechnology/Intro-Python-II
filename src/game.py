import sys
from player import Player
from room import Room


INVALID_INPUT_WARNING = "<Invalid input; please try again>"


class Game:
    '''The game'''
    def __init__(self, player: Player, rooms: list(Room)):
        self.player = player
        self.rooms = rooms
        self.__playing = False

    def start(self):
        '''Begin the game'''
        self.__playing = True
        print("\n\n-- ADVENTURE GAME --\n\n\n")

        print("(Enter 'q' at any time to quit.)")
        while self.__playing:
            self.__update()

    def stop(self):
        '''End the game'''
        self.__playing = False

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
            self.__parse_get(" ".join(split_txt))
        if verb == "drop":
            self.__parse_drop(" ".join(split_txt))

    def __parse_move(self, txt):
        possible_room = self.player.current_room.get_room_in_direction(txt)
        if possible_room is None:
            print(INVALID_INPUT_WARNING)
        else:
            self.player.current_room = possible_room

    def __parse_get(self, item_name):
        for item in self.player.current_room.items_list:
            if item.name == item_name:
                self.player.take_item(item)
                return
        __bad_get(item_name)

    def __parse_drop(self, item_name):
        for item in self.player.items_list:
            if item.name == item_name:
                self.player.drop_item(item)
                return
        __bad_drop(item_name)

    @property
    def playing(self):
        '''True if the game is running, false if not'''
        return self.__playing


def __bad_get(item):
    print(f"<There's no '{item}' in the room>")


def __bad_drop(item):
    print(f"<There's no '{item}' in your inventory>")
