# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
  def __init__(self, name='player', rm_nickname='outside'):
    self.name = name
    self.rm_nickname = rm_nickname

  def __repr__(self):
    return "Welcome {}! You are approaching the {}".format(self.name, self.rm_nickname)
