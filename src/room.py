# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
  def __init__(self, name='unknown', description='darkness surrounds you'):
    self.name = name
    self.description = description

  def __repr__(self):
    return "Current room: {}; Room description: {}".format(self.name, self.description)
