# Base class for specialized item types to be declared later.

# Item Superclass
class Item:
  def __init__(self, type, descriptor, description, can_get = True):
    self.type = type
    self.name = type
    self.descriptor = descriptor # Adjective like color, or quantity
    self.description = description
    self.can_get = can_get
  
  # Get Item
  def on_get(self, player):
    print(f'\nYou pick up the {self.type} and add it to your bag.')
    player.items.append(self)
    player.location.items.remove(self)
  
  # Drop Item
  def on_drop(self, player):
    print(f'\nYou drop the {self.type}')
    player.location.items.append(self)
    player.items.remove(self)

  # Check Item
  def on_check(self, player):
    print(f"\nExamining the {self.type}, you see...")
    print(self.description)

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

# Feature Subclass
class Feature(Item):
  def __init__(self, type, descriptor, description):
    super().__init__(type, descriptor, description, False)