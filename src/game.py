from player import Player


INVALID_INPUT_WARNING = "<Invalid input; please try again>"


class Game:
    '''The game'''
    def __init__(self, player: Player, rooms: dict):
        self.player = player
        self.rooms = rooms
        self.__playing = False

    def start(self):
        '''Begin the game'''
        self.__playing = True
        print("\n\n-- ADVENTURE GAME --\n\n\n")

        print("Enter 'n', 's', 'e', or 'w' to move in a cardinal direction.")
        print("Enter 'i' or 'inventory' to show your items in hand.")
        print("Enter 'q' at any time to quit.")

        while self.__playing:
            self.__update()

    def stop(self):
        '''End the game'''
        self.__playing = False

    @property
    def playing(self):
        '''True if the game is running, false if not'''
        return self.__playing

    def __update(self):
        print("\n" + self.player.current_room.name)
        print(self.player.current_room.description)

        txt = input("<Move the player>: ")
        self.__parse_input(txt)

    def __parse_input(self, txt: str):
        if txt == 'q':
            self.__playing = False
            print("Quitting...")
        elif txt in ('i', 'inventory'):
            print(f"Inventory: {self.player.inventory}")
        elif len(txt) == 1:
            self.__parse_move(txt)
        else:
            self.__parse_action(txt)

    def __parse_action(self, txt: str):
        split_txt = txt.split()
        verb = split_txt.pop(0)
        if verb in ("get", "take"):
            self.__parse_get(" ".join(split_txt))
        elif verb == "drop":
            self.__parse_drop(" ".join(split_txt))
        else:
            print(INVALID_INPUT_WARNING)

    def __parse_move(self, txt: str):
        possible_room = self.player.current_room.get_room_in_direction(txt)
        if possible_room is None:
            print(INVALID_INPUT_WARNING)
        else:
            self.player.enter_room(possible_room)

    def __parse_get(self, item_name: str):
        for item in self.player.current_room.items_list:
            if item.name == item_name:
                self.player.take_item(item)
                return
        print(f"<There's no '{item_name}' in the room>")

    def __parse_drop(self, item_name: str):
        for item in self.player.items_list:
            if item.name == item_name:
                self.player.drop_item(item)
                return
        print(f"<There's no '{item_name}' in your inventory>")
