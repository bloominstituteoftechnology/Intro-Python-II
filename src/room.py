# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
  def __init__(self, name, description, exits):
    self.name = name
    self.description = description
    self.exits = exits
    self.n_to = None
    self.s_to = None
    self.e_to = None
    self.w_to = None

  def __str__(self):
    return f"you find {self.name}, yourself at  {self.description}"