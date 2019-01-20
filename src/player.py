# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
  def __init__(self, name, location, last_location = None, items = []):
    self.name = name
    self.location = location
    self.last_location = last_location
    self.items = items
  
  def inventory(self):
    # Check if there are any items in inventory
    if len(self.items) > 0:
      print('\nYou are carrying:\n')
      for item in self.items:
        print(item.name)
    else:
      print("\nYou aren't carrying anything!\n")