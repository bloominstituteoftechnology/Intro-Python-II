# Write a class to hold player information, e.g. what room they are in
# currently.
import random

class Player:
    def __init__(self, currentRoom):
        self.currentRoom = currentRoom
        self.inventory = []

    def get(self, item):
        if len(self.inventory) < 4 and item.hidden == False:
            self.inventory.append(item)
            self.currentRoom.items.remove(item)
            print(f'Picked up {item.name}')
        elif item.hidden == False:
            print(f'There is no {item}')
        elif self.inventory >= 4:
            print(f'Can\'t pick up {item.name}, inventory full')

    def drop(self, item):
        self.inventory.remove(item)

    def investigate(self):
        search = random.randint(0, 100)

        for secret in self.currentRoom.secrets:
            if secret.difficulty <= search:
                secret.hidden = False
                print(f'Found: \n{secret} \nTo pick up enter "{secret.name}"')