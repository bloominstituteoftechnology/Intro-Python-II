"""
BeWilder - text adventure game :: Player definition

Write a class to hold player information.
e.g. what room they are in currently.
"""

import sys

from adv_utils import table_maker
from item import Item, Food, Artifact, Weapon, Armor
from room import Room


class Player:
    def __init__(self, name: str, current_room: Room):
        """Constructor for the Player base class.
        
        :param current_room (str) : The player's current room, defaults to 'outside'.
        """
        self.name = name
        # Set the initial room by "moving" into it, thus printing the room info
        self.move(current_room)
        # Set up items attributes
        self.items = []
        self.hp = 100
        self.defense = 0
        self.offense = 0

    def move(self, dst_room: Room):
        """Moves the player to a new room.
        
        :param dst_room (Room) : The player's destination room.
        """
        self.current_room = dst_room
        # Print room data: name, description, and items
        print(f"\n{self.current_room}")

    def take_action(self, cmd: str):
        """Take action by key command.
        
        :param cmd (str) : Key command from user.
        :param player (Player) : Instance of Player which will take the action.
        :return (None) : Calls the appropriate function.
        """
        # Look up destination room and move the player into it
        dst = getattr(self.current_room, f"{cmd}_to")
        self.move(dst) if dst else print("No room exists in that direction!")

    def get_item(self, item: Item):
        if isinstance(item, Item):
            if item in self.current_room.items:
                self.items.append(item)
                print(f"\n{item.name} added to inventory.")
            else:
                print("Item unavailable.")
        else:
            print("\nItem acquisition failed!")
            print("You can only add items to your inventory.")

    def inventory(self):
        title = f"{self.name}'s current inventory"
        # Create dictionary of item names and descriptions
        item_dict = {item.name: item.description for item in self.items}
        # Use that dictionary to generate a table
        print_string = table_maker(item_dict, title, 20, 20)
        print(print_string)

    def use_item(self, item: Item):
        if isinstance(item, Food):
            self.hp += item.calories
            print(f"You consumed {item.name}, your hp is now {self.hp}")
            self.items.remove(item)
        # TODO: Armor adds defense
        # TODO: Weapon adds offense
