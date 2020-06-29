# Write a class to hold player information, e.g. what room they are in
# currently.
class Player():
  def __init__(self, name, current_room):
    self.name = name
    self.current_room = current_room
    self.inventory = []

  def get_item(self, item):
    self.inventory.append(item)

  def dropped_item(self, item_name):
    for i in self.inventory:
      if i.name == item_name:
        self.inventory.remove(i)
        return True
    return False

  def print_inventory(self):
    if len(self.inventory) < 1:
      print("Your inventory is empty")
    for i in self.inventory:
      print(i)

  def __str__(self):
    return f"I am in {self.current_room}"