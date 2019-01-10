# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
  def __init__(self, name='unknown', description='Darkness surrounds you'):
    self.name = name
    self.description = description

  def __repr__(self):
    return "You are approaching the {}. {}".format(self.name, self.description)

  def get_room_name(self):
    return self.name

  def get_description(self):
    return self.description
  

