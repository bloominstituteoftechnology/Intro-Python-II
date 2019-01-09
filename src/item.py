# Base class for specialized item types to be declared later.

class Item:
  def __init__(self, name, description):
    self.name = name
    self.description = description