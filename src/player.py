from item import Item, LightSource
# Write a class to hold player information, e.g. what room they are in
# currently.
Lamp = LightSource("Lamp", "A Bug Lamp is a miscellaneous item in The Elder Scrolls III: Morrowind. This item provides a portable light source which can be carried in the left hand while traveling.")

class Player():
    def __init__(self, name=None, current_room=None, inventory=[]):
        self.name = name
        self.current_room = current_room
        self.inventory = inventory

    def __str__(self):
        return (f"{self.name} {self.current_room}")

    def move_player(self, direction):
        move = f"{direction}"
        current_room = self.current_room
        if direction == "n" and current_room.n_to != None:
            self.current_room = current_room.n_to
            return True
        if direction == "s" and current_room.s_to != None:
            self.current_room = current_room.s_to
            return True
        if direction == "e" and current_room.e_to != None:
            self.current_room = current_room.e_to
            return True
        if direction == "w" and current_room.w_to != None:
            self.current_room = current_room.w_to
            return True
        else:
            return False
    
    def describe_room(self):
        print (f"\n    {self.current_room.name.upper()}    \n\n{self.current_room.description} \n")

    def check_inventory(self):
        if len(self.inventory) == 0:
            print("\n You currently don't have any items. \n")
        else:
            print ("\n The items you have: ")
            for i in self.inventory:
                print (f"\n · {(i.name).upper()} \n{i.description}\n")

    def pick_item(self, item):
        self.inventory.append(item)
        print(f"\n You have picked up {item.name}. \n")

    def drop_item(self, item):
        if len(self.inventory) == 0:
            print("\n You currently don't have any items. \n")
        elif item in self.inventory:
            self.inventory.remove(item)
            print(f"\n You have dropped {item.name}. \n")

    def is_light_on(self):
        # if len(self.inventory) == 0:
        #     print("\n It's dark here. You need to get some light. \n")
        a = 0
        for i in self.inventory:
            a += 1
            if i.name == Lamp.name:
                print("\n The Light is ON! \n")
        if a == 0:
            print("\n It's dark here. You need to get some light. \n")



