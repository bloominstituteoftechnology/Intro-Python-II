# Write a class to hold player information, e.g. what room they are in
# currently.
from textwrap import wrap


class Player:
    """
    < Player > interacts with adventure REPL
    """
    information = {"name": "", "room": "", "map": ""}
    items = []

    def __init__(self, **kwargs):
        self.information = kwargs

    def __str__(self):
        return f'<Player: {self.name()}>'

    def status(self):
        """
        [< Player > name]  [< Room > name]
        """
        name = self.name()
        room = self.room()
        text_space = ' ' * (42 - (len(name) + len(room) + 16))
        return f'\n[NAME: {name}]' + text_space + f'[ROOM: {room}]\n'

    def name(self):
        """
        name of < Player >
        """
        return self.information["name"]

    def room(self):
        """
        < Room > that < Player > currently occupies
        """
        try:
            ret = self.information["room"].name
        except AttributeError as e:
            ret = e
        return ret

    def look(self):
        """
        < Player > looks around < Room >
        """
        desc = "\n".join(wrap(self.information["room"].description, 42))
        return f'{desc}\n' + '*'*42

    def path(self, thisway, fromHere):
        """
        < Player > scouts the path from
        < Room > leading [thisway]
        """
        return getattr(fromHere, thisway[0] + '_to', "blocked!")

    def walk(self, thisway):
        """
        < Player > walks [thisway]
        """
        room = self.information["room"]
        next_room = self.path(thisway, room)
        if next_room != "blocked!":
            print(f'\nOK, you travel {thisway}')
            self.information["room"] = next_room
        else:
            print(f'\nERROR, you cannot go {thisway}')

    def getItem(self, itemName):
        """
        < Player > takes < Item: [itemName] > from < Room >
        """
        room = self.information["room"]
        item = room.takeItem(itemName)
        if item:
            self.items.append(item)
            print(f'INVENTORY : {self.items}')
        else:
            print(f'cannot take {itemName}')

    def evaluate(self, cmd):
        """
        process user input
        """
        # * Split the entered command and see if it has 1 or 2 words in it to determine
        #  if it's the first or second form.
        actions = cmd.split(" ")
        if len(actions) == 1:
            # single word actions
            if cmd in ["north", "n", "south", "s", "east", "e", "west", "w"]:
                self.walk(cmd)
            elif cmd == "start":
                hr = "*" * 42
                print(f"{hr}\n   The Adventure of 𝝺\n{hr}")
        elif len(actions) == 2:
            # double word actions
            verb, noun = actions
            if verb.lower() == "get":
                self.getItem(noun)


if __name__ == "__main__":
    print('creating a Player')
    newPlayer = Player(name="Player Test")
    print(newPlayer)
