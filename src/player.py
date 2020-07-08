# class for player information and attributes
from collections import defaultdict

class Adventurer:
    def __init__(self, room):
        self.room = room
        self.inventory = defaultdict(int)
    def __str__(self):
      return f"The adventurer is in room {self.room}"

    def OpenInventory(self):
        if len(self.inventory) > 0:
            for item in self.inventory:
                print(f"You are holding: {item.name}")
        else:
            print("You currently have nothing in your inventory") 