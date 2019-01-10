# Write a class to hold player information, e.g. what room they are in
# currently.

class Player():
  def __init__(self, name='Alice', rm_nickname='outside', inventory=[]):
    self.name = name
    self.rm_nickname = rm_nickname
    self.inventory = inventory

  def __repr__(self):
    return "\n{}, are you lost? You are nearing the {}. Inside your pockets there {} {} a crumb from the blueberry muffin you had this morning\n".format(
      self.name, 
      self.rm_nickname, 
      'are' if len(self.inventory) > 1 else 'is', 
      'nothing but' if not self.inventory else f'{self.inventory} and')

  def get_name(self):
    return self.name

  def get_room(self):
    return self.rm_nickname

  def get_inv(self):
    return self.inventory

  def add_item(self, added):
    self.added = added
    self.inventory.extend(added)
    return self.inventory

  def drop_item(self, dropped):
    self.dropped = dropped
    self.inventory.remove(dropped)
    return self.inventory

  def set_room(self, new_room):
    self.new_room = new_room
    self.rm_nickname = new_room
    return self.rm_nickname

  def return_outside(self):
    self.rm_nickname = 'outside'
    return  self.rm_nickname

