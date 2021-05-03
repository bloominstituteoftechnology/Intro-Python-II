# Write a class to hold player information, e.g. what room they are in
# currently.

from typing import Optional, Dict

from room import Room
from item import Item


class Player:
    def __init__(self,
                 name: str,
                 current_room: Optional[Room] = None,
                 inventory: Optional[Dict[Item, int]] = None
                 ):
        self.name = name
        self.current_room = current_room
        self.inventory = inventory if inventory is not None else {}

    def __str__(self):
        return f"""
        -----------------
        Player
        -----------------
        name: {self.name}
        current_room: {self.current_room}
        inventory: {self.inventory}
        -----------------
        """

    def grab_item(self, item: Item):
        if item not in self.inventory:
            self.inventory[item] = 0
        self.inventory[item] += 1

        # print(f'\nYou now have the {item.name} in your inventory.')
        # print(f'  * Your current inventory:\n    {self.inventory}')

    def drop_item(self, item: Item):
        if item.name not in self.inventory:
            return

        self.inventory[item] -= 1
        if self.inventory[item] == 0:
            del self.inventory[item]

        print(f'  * {item} has been removed from your inventory.')