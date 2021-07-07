# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
  def __init__(self, name, description, items):
    self.name = name
    self.description = description
    self.n_to = None
    self.e_to = None
    self.s_to = None
    self.w_to = None
    self.inventory = items
  def __str__(self):
    return self.name + '\n' + self.description + '\n'
  def addItem(self, item):
    self.inventory.append(item)
  def removeItem(self, item):
    try:
      self.inventory.remove(item)
      return True
    except ValueError:
      print('**ERROR**')
      return False