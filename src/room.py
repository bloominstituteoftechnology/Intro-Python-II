# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
  def __init__(self, name, description, inventory):
    self.name = name
    self.description = description
    self.inventory = inventory

  def __repr__(self):
    return "You are approaching the {}.\n{}\n\nYou see {}\nthe shadow of the White Rabbit".format(
      self.name, 
      self.description, 
      'nothing but ...' if not self.inventory else f'{self.inventory[0]} and')


  def get_room_name(self):
    return self.name

  def get_description(self):
    return self.description
  
  def get_inventory(self):
    return self.inventory

  def item_taken(self, taken):
    self.taken = taken
    self.inventory.remove(self.taken)
    return self.inventory

  def item_dropped(self, dropped):
    self.dropped = dropped
    self.inventory.append(self.dropped)
    return self.inventory
  

