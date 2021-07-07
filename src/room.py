# Implement a class to hold room information. This should have name and
# description attributes.
from item import Inventory

class Room:
  def __init__(self, name, description, n_to = None, s_to = None , e_to = None, w_to = None, items = None):
    self.name = name
    self.description = description
    self.n_to = n_to
    self.s_to = s_to
    self.e_to = e_to
    self.w_to = w_to
    if items is None:
      self.items = {}
    else:
      self.items = items
  
  def __str__(self):
    return "{}, {}".format(self.name, self.description)
  
  def room_items(self):
    if int(len(self.items)) > 0:
      print(f"You can see {int(len(self.items))} item(s) in this room\n\nItems: ")
      count = 0
      for name, description in self.items.items():
        if int(count) < int(len(self.items))-1: 
          print(f"{name}: {description} | ", end ='')
          count += 1
        elif int(count) == int(len(self.items))-1 and int(len(self.items))-1 != 0:
          print(f"and {name}: {description}")
        else:
          print(f"a(n) {name}: {description}")
    else:
      print("There are no items in this location.")


# test = Room('Sunroom', 'Spacious and bright.', items = {'Candle': 'Looks new', 'Book': 'Old and warn'})
# print(test.room_items())

