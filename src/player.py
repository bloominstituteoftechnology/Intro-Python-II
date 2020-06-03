# Write a class to hold player information, e.g. what room they are in
# currently.

class Player():

    def __init__(self, name, current_room):
        self.name = name
        self.inventory = []
        self.__current_room = current_room

    # Methods

    def show_inventory(self):
        print("Inventory:")
        for item in self.inventory:
            print(item.description)

    # Getter and Setter method

    def take(self, item):
        if item:
            self.inventory.append(item)
            item.on_take()

    def drop(self, inv):
        i = inv - 1
        if not self.inventory:
            print("Inventory is empty")
            return None
        self.inventory[i].on_drop()
        return self.inventory.pop(i)

    def get_current_room(self):
        return self.__current_room

    def set_current_room(self, room):
        if room:
            self.__current_room = room
        else:
            print("\nThere's nothing in this direction! (Use m to open your map\n")
            self.__current_room = self.__current_room
            if input("Continue..."): return

    current_room = property(get_current_room, set_current_room)