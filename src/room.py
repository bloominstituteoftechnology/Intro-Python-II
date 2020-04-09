# Implement a class to hold room information. This should have name and
# description attributes.


class Room():
    def __init__(self, name="default name", description="default description", n_to=None, e_to=None, s_to=None, w_to=None, inventory=None):
        self.name = name
        self.description = description
        self.n_to = n_to
        self.e_to = e_to
        self.s_to = s_to
        self.w_to = w_to
        self.inventory = inventory
        if self.inventory == None:
            self.inventory = []

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)

    def __repr__(self):
        return str(self.__class__) + ": " + str(self.__dict__)

    def removeItem(self, itemToRemove):
        if itemToRemove in self.inventory:
            self.inventory.remove(itemToRemove)

    def addItem(self, newItem):
        self.inventory.append(newItem)

    def printInventory(self):
        if self.inventory.__len__() <= 0:
            pass
        else:
            print("You take a moment to scan the room for objects.\nYou notice: ")
            # print(self.inventory[0].name)
            for item in self.inventory:
                print(f'\n{item.name}, {item.description}')

    def printStats(self):
        print(f"You are in the {self.name}. \n\"{self.description}\"")
        self.printInventory()
