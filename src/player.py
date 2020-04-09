# Write a class to hold player information, e.g. what room they are in
# currently.


class Player():
    def __init__(self, room, inventory=None):
        self.room = room
        self.inventory = inventory
        if self.inventory == None:
            self.inventory = []

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)

    def __repr__(self):
        return str(self.__class__) + ": " + str(self.__dict__)

    def moveTo(self, direction):
        if str(str.lower(direction[0:1:1])) == "n" and self.room.n_to != None:
            self.room = self.room.n_to
        elif str(str.lower(direction[0:1:1])) == "e" and self.room.e_to != None:
            self.room = self.room.e_to
        elif str(str.lower(direction[0:1:1])) == "s" and self.room.s_to != None:
            self.room = self.room.s_to
        elif str(str.lower(direction[0:1:1])) == "w" and self.room.w_to != None:
            self.room = self.room.w_to
        else:
            print("You cannot move in this direction!")

    def takeItem(self, itemNameToTake):
        if self.room.inventory.__len__() <= 0:
            print("There is nothing in this room!")
        else:
            for item in self.room.inventory:
                if str.lower(item.name) == itemNameToTake:
                    self.inventory.append(item)
                    self.room.removeItem(item)
                else:
                    print("Invalid item.")

    def dropItem(self, itemNameToDrop):
        if self.inventory.__len__() <= 0:
            print("You don't have any items!\n")
        else:
            for item in self.inventory:
                if str.lower(item.name) == itemNameToDrop:
                    print(f"You drop the {item.name}.")
                    self.inventory.remove(item)
                    self.room.addItem(item)
