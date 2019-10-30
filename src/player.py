# Write a class to hold player information, e.g. what room they are in
# currently.
import random


class Player(object):
    """Game character"""
    def __init__(self, name, hp=100, attack=5, weight_limit=50):
        self.name = name
        self.items = {}
        self.current_room = None
        self.hp = hp
        self.attack = attack
        self.shield = 0
        self.weight = 0
        self.weight_limit = weight_limit

    def move(self, direction):
        valid_move = eval(f'self.current_room.to_{direction}')
        if valid_move:
            self.current_room = valid_move
            self.print_position()
        else:
            ways = {'n': 'North', 's': 'South', 'w': 'West', 'e': 'East'}
            print(f"There is no room to the {ways[direction]}. \n")
            self.print_position()

    def action(self):
        # TODO: make this.
        pass

    def print_position(self):
        print(f"{self.current_room.name} \n{self.current_room.description} \n")

    def look(self):
        print(f"I can see {self.current_room.items}")

    def get(self, item):
        if self.weight + item.weight <= self.weight_limit:
            self.items[item.name] = item
            self.weight += item.weight
            self.current_room.items.pop(item.name, None)
            print(f"I have added the {item.name} to the inventory. \n")
        else:
            print(f"I'm carrying too much weight to add {item.name}")
            print(f"Current inventory weight: {self.weight}")
            print(f"Item weight: {item.weight}")
            print(f"Current weight limit: {self.weight_limit} \n")

    def take(self, item, character):
        if self.weight + item.weight <= self.weight_limit and self.hp > character.hp:
            self.items[item.name] = item
            self.weight += item.weight
            character.items.pop(item.name, None)
            print(f"I have taken the {item.name} and added it to the inventory. \n")
        else:
            print("I'm carrying too much weight to add this item")
            print(f"Current inventory weight: {self.weight}")
            print(f"Item weight: {item.weight}")
            print(f"Current weight limit: {self.weight_limit} \n")

    def drop(self, item):
        if item.name in self.items:
            self.items.pop(item.name, None)
            self.weight -= item.weight
            self.current_room.items[item.name] = item
            print(f"I have dropped {item.name}")
        else:
            print(f"I don't have {'an' if item.name.sartswith(('a', 'e', 'i', 'o', 'u', 'h')) else 'a'} {item.name} \n")

    def slash(self, character):
        if random.randint(0, 10) & 1:
            character.hp -= (self.attack - character.sheild)
            if character.hp <= 0:
                character.die()
            print(f"You slash {character.name}! Their health is now {character.hp} \n")
        else:
            print(f"You missed! \n")

    def use(self, item):
        pass

    def die(self):
        for item in self.items:
            self.current_room.items[item.name] = item
        print(f"{self.name} has died! Now littered about the room are {self.items.keys()} \n")

# 'move', 'look', 'get', 'take', 'drop', 'slash', 'use'
