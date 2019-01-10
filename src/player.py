# Write a class to hold player information, e.g. what room they are in
# currently.

class Player():
  def __init__(self, name='Alice', rm_nickname='outside'):
    self.name = name
    self.rm_nickname = rm_nickname

  def __repr__(self):
    return "\n{}, are you lost? You are nearing the {}.\n".format(self.name, self.rm_nickname)

  def get_name(self):
    return self.name

  def get_room(self):
    return self.rm_nickname

  def set_room(self, new_room):
    self.new_room = new_room
    self.rm_nickname = new_room
    return self.rm_nickname

  def return_outside(self):
    self.rm_nickname = 'outside'
    return  self.rm_nickname

