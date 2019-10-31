# Write a class to hold player information, e.g. what room they are in
# currently.
import random


class Player(object):
    """Game character.

    :var name: str - Player name
    :var hp: int - default 100
    :var attack: int - default 5
    :var weight_limit: int - default 50

    """

    def __init__(self, name: str, hp: int = 100, attack: int = 5, weight_limit: int = 50) -> None:
        self.name = name
        self.items_ = {}
        self.current_room = None
        self.hp = hp
        self.attack = attack
        self.shield = 0
        self.weight = 0
        self.weight_limit = weight_limit

    def __repr__(self) -> str:
        return f"Player({repr(self.name)})"

    def __str__(self) -> str:
        return f"{self.name.title()}\n{self.__dict__}"

    def move(self, *args: str) -> None:
        """Move Player from one room to the next.

        :var args: str the position to move to
        """
        if not args[0]:
            print("Please tell me where you want to move. \n")
            print("Valid directions are 'n', 's', 'e', 'w'")
            print("To move North type: 'move n' \n")
            return
        direction = args[0][0]
        if direction in ['n', 's', 'e', 'w']:
            valid_move = eval(f'self.current_room.to_{direction}')
            if valid_move:
                self.current_room.characters.pop(self.name, None)
                self.current_room = valid_move
                self.current_room.characters[self.name] = self
                self.print_position()
            else:
                ways = {'n': 'North', 's': 'South', 'w': 'West', 'e': 'East'}
                print(f"There is no path to the {ways[direction]}. \n")
                # self.print_position()

    def print_position(self) -> None:
        """Print the current room and its description."""
        print(f"{self.current_room.name} \n{self.current_room.description} \n")

    def look(self, *args) -> None:
        """Look in current room for available items.

        :var args: unused
        """
        if self.current_room.light or any(item.is_light and item.active for item in self.items_.values()):
            if self.current_room.items_:
                print("I can see:")
                for val in self.current_room.items_.values():
                    print(val)
            else:
                print(f"I don't see anything notable here.")
        else:
            print("It's too dark in here to see anything.")
        print()

    def get(self, *args: str) -> None:
        """Collect item named in args.

        :var args: str - item to be got.
        """
        if not args[0]:
            print("Please tell me what you want to get. \n")
            return
        item_name = args[0][0]
        if item_name in self.current_room.items_:
            item = self.current_room.items_[item_name]
            if self.weight + item.weight <= self.weight_limit:
                self.items_[item.name] = item
                self.weight += item.weight
                self.current_room.items_.pop(item.name, None)
                item.on_get()
            else:
                print(f"I'm carrying too much weight to add {item.name}")
                print(f"Current inventory weight: {self.weight}")
                print(f"Item weight: {item.weight}")
                print(f"Current weight limit: {self.weight_limit} \n")
        else:
            print(f"I don't see {'an' if item_name.startswith(('a', 'e', 'i', 'o', 'u')) else 'a'} {item_name}")

    def take(self, item: str, character: str) -> None:
        """Take item from another Player.

        :var item: str - item to be taken
        :var character: Player to take from
        """
        # if self.weight + item.weight <= self.weight_limit and self.hp > character.hp:
        #     self.items_[item.name] = item
        #     self.weight += item.weight
        #     character.items.pop(item.name, None)
        #     print(f"I have taken the {item.name} and added it to the inventory. \n")
        # else:
        #     print("I'm carrying too much weight to add this item")
        #     print(f"Current inventory weight: {self.weight}")
        #     print(f"Item weight: {item.weight}")
        #     print(f"Current weight limit: {self.weight_limit} \n")
        pass

    def drop(self, *args: str) -> None:
        """Drop item in current room.

        :var args: str - item to drop
        """
        if not args[0]:
            print("Please tell me what you want to drop. \n")
            return
        item_name = args[0][0]
        if item_name in self.items_:
            item = self.items_[item_name]
            if item.name in self.items_:
                self.items_.pop(item.name, None)
                self.weight -= item.weight
                self.current_room.items_[item.name] = item
                print(f"I have dropped {item.name} \n")
        else:
            print(f"I don't have {'an' if item_name.startswith(('a', 'e', 'i', 'o', 'u')) else 'a'} {item_name} \n")

    # def slash(self, character):
    #     if random.randint(0, 10) & 1:
    #         character.hp -= (self.attack - character.shield)
    #         if character.hp <= 0:
    #             character.die()
    #         print(f"You slash {character.name}! Their health is now {character.hp} \n")
    #     else:
    #         print(f"You missed! \n")

    def use(self, *args: str) -> None:
        """Use an item.

        Parse string and call appropriate method

        :var args: str - the name of the item to use
        """
        if not args[0]:
            print("Please tell me what you want to use. \n")
            return
        item_name = args[0][0]
        if item_name in self.items_:
            self.items_[item_name].active = True
        if 'key' in item_name:
            self._unlock_box(item_name)

    def _unlock_box(self, key_name: str) -> None:
        """Unlock a box in the room if Player has the correct color key.

        :var key_name: the name of the key i.e. 'black_key'
        """
        color = key_name.split('_')[0]
        if eval(f"'{color}_lock_box' in self.current_room.items_"):
            box_name = f"{color}_lock_box"
            if self.current_room.items_[box_name].key is self.items_[key_name]:
                self.current_room.items_[box_name].locked = False
                for item in self.current_room.items_[box_name].items_.values():
                    self.current_room.items_[item.name] = item
                print(f"I have unlocked the {box_name} \n")
        else:
            print(f"I don't see anything that this key fits. \n")

    def die(self) -> None:
        """Player has died, drop all items."""
        for item in self.items_:
            self.current_room.items_[item.name] = item
        print(f"{self.name} has died! Now littered about the room are {self.items_.keys()} \n")

    def inventory(self, *args) -> None:
        """Print out all items in Player items_.

        :var args: unused
        """
        print(f"Current weight: {self.weight} / {self.weight_limit}")
        if self.items_:
            for item in self.items_.values():
                print(f'Item: {item.name} - Weight: {item.weight}')
        else:
            print("I don't seem to have anything.")
