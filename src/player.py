# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
  def __init__(self, name, location, items = {}):
    self.name = name
    self.location = location
    self.items = items
  
  def inventory(self):
    # Check if there are any items in inventory
    if len(list(self.items.keys())) > 0:
      print('\nYou are carrying:\n')
      for item in self.items:
        print(self.items[item].name)
    else:
      print("\nYou aren't carrying anything!\n")