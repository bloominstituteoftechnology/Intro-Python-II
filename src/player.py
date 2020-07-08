# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
  def __init__(self, name, current_room):
    self.name = name
    self.current_room = current_room
    self.inventory = []
  
  def __str__(self):
    return f'{self.current_room} \n'

  def pickup_item(self, item):
      self.inventory.append(item)
      self.current_room.items.remove(item)
      print(f'You picked up {item.name}. \n')

  def drop_item(self, item):
    self.current_room.items.append(item)
    self.inventory.remove(item)


  def show_inventory(self):
    print(f'You have {self.inventory} in your inventory')

  