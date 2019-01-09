# Base class for specialized item types to be declared later.

class Item:
  def __init__(self, name, description):
    self.name = name
    self.description = description
  
  # Get Item
  def on_get(self):
    print(f'\nYou pick up the {self.name} and add it to your bag.')
  
  # Drop Item
  def on_drop(self):
    print(f'\nYou drop the {self.name}')