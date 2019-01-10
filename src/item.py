# Base class for specialized item types to be declared later.

# Item Superclass
class Item:
  def __init__(self, type, descriptor, description):
    self.type = type
    self.name = type
    self.descriptor = descriptor
    self.description = description
  
  # Get Item
  def on_get(self, player, room):
    print(f'\nYou pick up the {self.type} and add it to your bag.')
  
  # Drop Item
  def on_drop(self, player, room):
    print(f'\nYou drop the {self.type}')

# Card Subclass
class Card(Item):
  def __init__(self, color, description):
    super().__init__("card", color, description)
    self.color = color
    self.name = color + " Card"

# Credits Subclass
class Credits(Item):
  def __init__(self, quantity, description):
    super().__init__("credits", quantity, description)
    self.quantity = quantity
    self.name = self.quantity + " Credits"