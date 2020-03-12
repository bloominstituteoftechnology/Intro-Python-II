# Write a class to hold player information, e.g. what room they are in
# currently.
import adv
from adv import *


class Player:
    def __init__(self, name, current_room, inventory=[]):
        self.name = name
        self.current_room = current_room
        self.inventory = inventory

    def pickup(self, itemname):
        for i in adv.items:
            if items[i].name.lower() == itemname.lower():
                item = items[i]
        lengther = len('You pick up !' + item.name)
        desc_length = len(item.description)
        print(f'\nYou pick up {item.name}!')
        print(f'''{'-'*lengther}''')
        self.inventory.append(item.name)
        self.current_room.item_names.remove(item.name)
        self.check_inv()

    def drop_item(self, itemname):
        for i in adv.items:
            if items[i].name.lower() == itemname.lower():
                item = items[i]
        lengther = len('You get rid of: ' + item.name + '!')
        print('-'*lengther)
        print(f'You get rid of: {item.name}!')
        print('-'*lengther)
        self.inventory.remove(item.name)
        self.current_room.item_names.append(item.name)
        self.check_inv()
    
    def inspect_item(self, itemname):
        for i in adv.items:
            if items[i].name.lower() == itemname.lower():
                item = items[i]
        item.describe()

    def move(self, direction):
        self.current_room = direction
        print(f'\nMoving to the {self.current_room.name}\n')

    def welcome_player(self):
        clear()
        lengther = len('You are currently in the ' + self.current_room.name)
        print(f'\nWelcome {self.name}!\n')
        print(
            f'''You are currently in the {self.current_room.name}\n{'-'*lengther}''')

    def self_describe(self):
        stats_len = len('Character Stats')
        name_len = len('Name: ' + self.name)
        room_len = len('Current Room: ' + self.current_room.name)
        inv_len = len(', '.join(self.inventory))
        empty_len = len('there is nothing in your inventory!')
        print('Character Stats')
        print(f'''{'-'*stats_len}
Name: {self.name}\n{'-'*name_len}
Current Room: {self.current_room.name}\n{'-'*room_len}
Inventory: ''')
        if self.inventory:
            print(*self.inventory, sep=', ')
            print('-'*inv_len)
        else:
            print('There is nothing in your inventory!')
            print('-'*empty_len)

    def check_inv(self):
        lengther = len(', '.join(self.inventory))
        empty_len = len('there is nothing in your inventory!')
        print('Inventory:')
        if self.inventory:
            print(*self.inventory, sep=', ')
            print('-'*lengther)
        else:
            print('There is nothing in your inventory!')
            print('-'*empty_len)
