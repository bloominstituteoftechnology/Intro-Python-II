# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
  def __init__(self, name, rName, items=None):
    self.name = name
    self.rName = rName
    if items is None:
      self.items = []
    else:
      self.items = items  

  def __str__(self):
    return f"Hi, {self.name} you are in {self.rName} room."

