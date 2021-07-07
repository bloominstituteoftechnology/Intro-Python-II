# Write a class to hold player information, e.g. what room they are in
# currently.

from item import LightSource


class Player:
    def __init__(self, current_room, hitpoints, attack):
        self.current_room = current_room
        self.inventory = []
        self.has_lightsource = False
        self.hitpoints = hitpoints
        self.attack = attack
        self.is_alive = True

    def take_item(self, item):
        if isinstance(item, LightSource):
            self.has_lightsource = True
        self.inventory.append(item)

    def drop_item(self, item):
        if isinstance(item, LightSource):
            self.has_lightsource = False
        self.inventory.remove(item)

    def show_inventory(self):
        print("You have the following items in your inventory:")
        for item in self.inventory:
            print(f"{item.name}: {item.description}")

    def move_to(self, room):
        if self.current_room != room:
            self.current_room = room
            if self.current_room.is_light or self.has_lightsource:
                print(f"You have now entered {room.name}. {room.description}")
            else:
                print("You've have changed location, but it's too dark to see anything.")

    def attack_monster(self, monster):
        if monster.is_alive:
            monster.hitpoints -= self.attack
            print(f"You did {self.attack} damage to {monster.name}, it now has {monster.hitpoints} HP left.")

            self.hitpoints -= monster.attack
            print(f"{monster.name} did {monster.attack} damage to you. You now have {self.hitpoints} HP left.")
            if self.hitpoints <= 0:
                self.is_alive = False

            if monster.hitpoints <= 0:
                monster.is_alive = False
                print(f"{monster.name} has been defeated!")

        else:
            print(f"{monster.name} is already dead.")
