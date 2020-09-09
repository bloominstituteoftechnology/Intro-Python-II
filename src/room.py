# Implement a class to hold room information. This should have name and description attributes.

from item import Item

class Room:
  def __init__(self, name, description):
    self.name = name
    self.description = description
    self.items = []

  def get_direction(self, direction):
    if direction == "n":
      print("\nYou walk North...\n")
      return self.n_to
    elif direction == "s":
      print("\nYou walk South...\n")
      return self.s_to
    elif direction == "e":
      print("\nYou walk East...\n")
      return self.e_to
    elif direction == "w":
      print("\nYou walk West...\n")
      return self.w_to
    else:
      return None
  
  def addItem(self, item: Item):
    self.items.append(item)