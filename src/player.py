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

    def __environment(self):
        return self.information["room"]

    def getRoom(self):
        return self.__environment()

    def room(self):
        """
        < Room > that < Player > currently occupies
        """
        try:
            ret = self.__environment().name
        except AttributeError as e:
            ret = e
        return ret

    def look(self):
        """
        < Player > looks around < Room >
        """
        desc = "\n".join(wrap(self.__environment().description, 42))
        contains = self.__environment().items
        if len(contains) > 0:
            itemNames = [x.name for x in self.__environment().items]
            itemNames[0] = f'you see a {contains[0].name}'
            csv = ", ".join(itemNames)
            items = "\n".join(wrap(csv, 42))
            desc += f"\n{items}"
        return f'{desc}\n' + '*'*42

    def path(self, thisway, fromHere):
        """
        < Player > scouts the path from
        < Room > leading [thisway]
        """
        return getattr(fromHere, thisway[0] + '_to', "blocked!")

    def enter(self, room):
        """
        < Player > enters < Room >
        """
        self.information["room"] = room

    def walk(self, thisway):
        """
        < Player > walks [thisway]
        """
        room = self.__environment()
        next_room = self.path(thisway, room)
        if next_room != "blocked!":
            print(f'\nOK, you travel {thisway}')
            self.enter(next_room)
        else:
            print(f'\nERROR, you cannot go {thisway}')

    def getItem(self, itemName):
        """
        < Player > takes < Item: [itemName] > from < Room >
        """
        container = self.__environment()
        item = container.takeItem(itemName)
        if item:
            self.items.append(item)
        else:
            print(f'you cannot take {itemName} from {container}')

    def dropItem(self, itemName):
        """
        < Player > drops < Item: [itemName] > in < Room >
        """
        room = self.__environment()
        dropped = self.inventory(itemName, dropping=True)
        result = '\n'.join([room.dropItem(item) for item in dropped])
        print(result)

    def inventory(self, itemName=None, dropping=False):
        if itemName is None:
            # select every element of Player.items
            selected = self.items
        else:
            # only select item(s) with the name given by "itemName"
            selected = list(filter(lambda i: i.name == itemName, self.items))
        if not dropping:  # without dropping anything,
            # return the selected item(s) for consideration;
            return list(enumerate(map(lambda i: i.name, selected)))
        # otherwise...
        dropped = []  # make a *new list to hold item(s) we want dropped.
        while len(selected) > 0:  # continue if we have items to remove.
            item = selected.pop()  # pop from selected.
            self.items.remove(item)  # remove from Player.items
            dropped.append(item)  # & add to our *new list
        return dropped  # finally, we return the *new list of dropped items

    def evaluate(self, cmd):
        """
        process user input
        """
        # * Split the entered command and see if it has 1 or 2 words
        #  to determine if it's the first or second form.
        actions = cmd.split(" ")
        if len(actions) == 1:
            # single word actions
            if cmd in ["north", "n", "south", "s", "east", "e", "west", "w"]:
                self.walk(cmd)
            elif cmd == "start":
                hr = "*" * 42
                print(f"{hr}\n   The Adventure of 𝝺\n{hr}")
            elif cmd in ["inventory", "i"]:
                print(f"{self.inventory()}")
        elif len(actions) == 2:
            # double word actions
            verb, noun = actions
            v = verb.lower()
            if v == "get":
                self.getItem(noun)
            elif v == "drop":
                self.dropItem(noun)
            elif v in ["inventory", "i"]:
                try:
                    idx = int(noun)  # try reading by index number
                    i = self.items[idx]
                    print(f"\n***{i.description}***\n")
                except ValueError:
                    i = self.inventory(noun)  # try reading by name
                    print(f"\n***{i}***\n")
                except Exception:
                    print(f"I cannot understand '{cmd}'")


if __name__ == "__main__":
    print('creating a Player')
    newPlayer = Player(name="Player Test")
    print(newPlayer)
