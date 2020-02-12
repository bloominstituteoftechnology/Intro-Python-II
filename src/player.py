from weapon import Weapon
from lightsource import Lightsource

fists = Weapon('fists', 'your bare hands', 1)

class Player:

    def __init__(self, name, current_room, items, weapon=fists, points=0):
        self.name = name
        self.current_room = current_room
        self.items = items
        self.weapon = weapon
        self.points = points

    def print_current_room(self):
        print(f"\nYou are currently at the {self.current_room.name}.")

    def check_lightsource(self):
        for i in self.items:
            if isinstance(i, Lightsource):
                if self.current_room.light is False:
                    # print("Your light source illuminates the darkness.")
                    self.current_room.light = False

    def look_around(self):
        """Examine the current room based on the light level and list contents."""
        if self.current_room.light is True:
            print(self.current_room.description + '\n')
            if len(self.current_room.items) == 1:
                print(f'You can see a {self.current_room.items[0]}.\n')
            elif len(self.current_room.items) > 1:
                print('You can see some items:\n')
                for item in self.current_room.items:
                    print(f"{item.name}: {item.description}")
            print("\n")
            if len(self.current_room.enemies) > 0:
                print(
                    f"Danger ahead! You can see a {self.current_room.enemies[0].name}.\n")
        else:
            print("It's pitch black! You can't see a thing!\n")

    def move(self, direction):
        """Try to move in the given direction. Accepts n, s, e, w."""
        if direction:
            if getattr(self.current_room, f"{direction}_to") != None:
                self.current_room = getattr(
                    self.current_room, f"{direction}_to")
        else:
            print("You can't move in that direction from here.\n")

    def take(self, action):
        """Try to take an item in the current room."""
        item_name = action[1]
        for i in self.current_room.items:
            if item_name == i.name:
                if isinstance(i, Weapon):
                    self.weapon = i
                i.on_take()
                self.items.append(i)
                self.current_room.items.remove(i)

    def drop(self, action):
        """Drop an item, removing it from inventory and adding it
        to the current room's list of items"""
        item_name = action[1]
        for i in self.items:
            if item_name == i.name:
                i.on_drop()
                self.items.remove(i)
                self.current_room.items.append(i)

    def inventory(self, action):
        """List current items if player has any."""
        if len(self.items) > 0:
            print(f"\nCurrently, in your inventory you have:")
            for item in self.items:
                print(f"{item.name}: {item.description}")
        else:
            print("Your pack is empty at the moment.")
        print("\n")
