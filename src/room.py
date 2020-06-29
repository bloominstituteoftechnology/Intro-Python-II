# Implement a class to hold room information. This should have name and
# description attributes.

class Room():
  def __init__(self, name, description):
    self.name = name
    self.description = description
    self.n_to = None
    self.s_to = None
    self.e_to = None
    self.w_to = None
    self.items = []

  def print_items(self):
    for i in self.items:
      print(i)

  def receive_item(self, item):
    self.items.append(item)

  def got_item(self, item_name):
    for i in self.items:
      if i.name == item_name:
        self.items.remove(i)
        return True
    return False

  def __str__(self):
      return f"Your Location: {self.name} - {self.description}"