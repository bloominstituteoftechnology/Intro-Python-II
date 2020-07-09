# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.items = []
    
    def __str__(self):
        return f'{self.current_room} \n'
    
    def pickupItem(self, item):
      self.items.append(item)
      self.current_room.items.remove(item)
      print(f'You picked up {item.name}. \n')
    
    def dropItem(self, item):
        self.current_room.items.append(item)
        self.items.remove(item)

    def show_inventory(self):
        print(f'You have {self.items} in your inventory')