# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, location, inventory):
        self.location = location
        self.inventory = inventory

    
    def addPlayerItem(self, item):
     self.inventory.append(item)
     print(f"You found {item} and added it to your inventory")

    def dropItem(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
        else:
            print(f"{item} is not in inventory")   
               
    def showItems(self):
        for i in self.inventory:
          print(i.name)      