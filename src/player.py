# Write a class to hold player information, e.g. what room they are in
# currently.
class Player: 
    def __init__(self, name, current_room):
      self.name = name
      self.current_room = current_room
      self.inventory = []
    def __str__(self):
      return f"<Player '{self.name}', is in room {self.current_room}>"
    
    def showInventory(self):
        if len(self.inventory) > 0:
            for item in self.inventory:
                print(item.name)
        else:
            print('You have nothing in your inventory')