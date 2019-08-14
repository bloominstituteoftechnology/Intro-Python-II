# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
  def __init__(self, name, description, n_to = None, s_to = None , e_to = None, w_to = None, items = None):
    self.name = name
    self.description = description
    self.n_to = n_to
    self.s_to = s_to
    self.e_to = e_to
    self.w_to = w_to
    self.items = items
  
  def __str__(self):
    return "{}, {}".format(self.name, self.description)
  
  def room_item(self):
    if self.items is not None:
      print(f"There are {int(len(self.items))} item(s) in this room\n")
      count = 0
      for i in self.items:
        if int(count) < int(len(self.items))-1: 
          print(f"{i}, ", end ='')
          count += 1
        elif int(count) == int(len(self.items))-1:
          print(f"and {i}")
    else:
      print("There are no items in this location.")


test = Room("foyer", "Very nice looking", items = ['hat', 'cat', 'coat', 'scarf'])

print(test.room_item())