# Write a class to hold player information, e.g. what room they are in
# currently.
from textwrap import wrap


class Player:
    information = {"name": "", "room": "", "map": ""}

    def __init__(self, **kwargs):
        self.information = kwargs

    def __str__(self):
        return f'<Player: {self.name()}>'

    def status(self):
        """
        the players name & the current room name
        """
        name = self.name()
        room = self.room()
        text_space = ' ' * (42 - (len(name) + len(room) + 16))
        return f'\n[NAME: {name}]' + text_space + f'[ROOM: {room}]\n'

    def name(self):
        """
        the players name
        """
        return self.information["name"]

    def room(self):
        """
        room that the player currently occupies
        """
        try:
            ret = self.information["room"].name
        except AttributeError as e:
            ret = e
        return ret

    def look(self):
        """
        the current description
        """
        desc = "\n".join(wrap(self.information["room"].description, 42))
        return f'{desc}\n' + '*'*42

    def path(self, thisway, fromHere):
        """
        find path
        """
        return getattr(fromHere, thisway[0] + '_to', "blocked!")

    def walk(self, thisway):
        """
        move the player
        """
        room = self.information["room"]
        next_room = self.path(thisway, room)
        if next_room != "blocked!":
            print(f'\nOK, you travel {thisway}')
            self.information["room"] = next_room
        else:
            print(f'\nERROR, you cannot go {thisway}')

    def evaluate(self, cmd):
        """
        If the user enters a cardinal direction, 
        attempt to move to the room there.

        Print an error message if the movement isn't allowed.
        """
        if cmd in ["north", "n", "south", "s", "east", "e", "west", "w"]:
            self.walk(cmd)
        elif cmd == "start":
            hr = "*" * 42
            print(f"{hr}\n   The Adventure of 𝝺\n{hr}")
