# Write a class to hold player information, e.g. what room they are in
# currently.
import random
import sys
from room import Arena


class Player(object):
    """Game character.

    :var name: str - Player name
    :var hp: int - default 100
    :var attackpts: int - default 5
    :var weight_limit: int - default 50

    """

    def __init__(self, name: str, hp: int = 100, attackpts: int = 5, weight_limit: int = 50) -> None:
        self.name = name
        self.items_ = {}
        self.current_room = None
        self.hp = hp
        self.attackpts = attackpts
        self.weight = 0
        self.weight_limit = weight_limit
        self.has_slingshot = False
        self.has_pebbles = False

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
                if isinstance(valid_move, Arena):
                    valid_move.battle()
            else:
                ways = {'n': 'North', 's': 'South', 'w': 'West', 'e': 'East'}
                print(f"There is no path to the {ways[direction]}. \n")
                # self.print_position()

    def print_position(self) -> None:
        """Print the current room and its description."""
        print(f"{self.current_room.name} \n{self.current_room.description} \n")

    def look(self, *args) -> None:
        """Look in current room for available items.

        Mark items seen as seen.
        :var args: unused
        """
        if self.current_room.light or any(item.is_light and item.active for item in self.items_.values()):
            self.current_room.light = True
            if self.current_room.items_:
                print("I can see:")
                for val in self.current_room.items_.values():
                    val.seen = True
                    print(val)
            else:
                print(f"I don't see anything notable here. \n")
        else:
            print("It's too dark in here to see anything. \n")
        print()  # Just a blank line for display purposes.

    def get(self, *args: str) -> None:
        """Collect item named in args.

        :var args: str - item to be got.
        """
        if not args[0]:
            print("Please tell me what you want to get. \n")
            return
        item_name = args[0][0]
        if item_name in self.current_room.items_ and self.current_room.items_[item_name].seen:
            item = self.current_room.items_[item_name]
            if self.weight + item.weight <= self.weight_limit:
                self.items_[item.name] = item
                self.weight += item.weight
                self.current_room.items_.pop(item.name, None)
                item.on_get(self)
            else:
                print(f"I'm carrying too much weight to add {item.name}")
                print(f"Current inventory weight: {self.weight}")
                print(f"Item weight: {item.weight}")
                print(f"Current weight limit: {self.weight_limit} \n")
        else:
            print(f"I haven't seen {'an' if item_name.startswith(('a', 'e', 'i', 'o', 'u')) else 'a'} {item_name} \n")

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

    def attack(self, character: 'Player') -> None:
        """Helper function to call _attack.

        :var character: The character to attack.
        """
        if self.has_pebbles and self.has_slingshot:
            self.items_['sling_shot'].shoot(character)
        else:
            self._attack(character)

    def _attack(self, character: 'Player') -> None:
        """Attack another character.

        :var character: The character to attack.
        """
        if random.randint(0, 10) & 1:
            character.hp -= self.attackpts
            if character.hp <= 0:
                character.die()
            print(f"{self.name} {'shoots' if self.has_slingshot and self.has_pebbles else 'hits'} "
                  f"{character.name}! Their health is now {character.hp} \n")
        else:
            print(f"{self.name} missed! \n")

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
        if 'sling' in item_name:
            self.items_[item_name].blank()
        if 'pebble' in item_name:
            self.items_[item_name].rock()
        if 'dog' in item_name:
            if 'doggo' in self.current_room.characters:
                print(f"You found the dog and gave them a treat! They'll be your friend forever now. "
                      f"You win! \n")
                sys.exit()
            else:
                print("I don't see any dogs around here. \n")
        if 'berrie' in item_name:
            self.items_[item_name].eat()

    def _unlock_box(self, key_name: str) -> None:
        """Unlock a box in the room if Player has the correct color key.

        :var key_name: the name of the key i.e. 'black_key'
        """
        color = key_name.split('_')[0]
        if eval(f"'{color}_lock_box' in self.current_room.items_"):
            box_name = f"{color}_lock_box"
            if (self.current_room.items_[box_name].seen and
                    self.current_room.items_[box_name].key is self.items_[key_name]):
                self.current_room.items_[box_name].locked = False
                for item in self.current_room.items_[box_name].items_.values():
                    self.current_room.items_[item.name] = item
                print(f"I have unlocked the {box_name} \n")
            else:
                print(f"I don't see anything that this key fits. \n")
        else:
            print(f"I don't see anything that this key fits. \n")

    def die(self) -> None:
        """Player has died, drop all items.

        If the user has died, exit the game.
        #TODO: make game reset and start over.
        """
        for item in self.items_.values():
            self.current_room.items_[item.name] = item
        if not self.name == 'The Bear':
            print(f"{self.name} has died! Now littered about the area "
                  f"are {[item.name for item in self.items_.values()]} \n")
            sys.exit()
        else:
            print("Take that The Bear! I win! \n")

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
        print()  # Blank line for display purposes.
