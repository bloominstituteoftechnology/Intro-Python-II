# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
  def __init__(self, name, description):
    self.rname = name
    self.rdescription = description
    self.n_to = None
    self.e_to = None
    self.s_to = None
    self.w_to = None
  def __str__(self):
    return 'You are currently: ' + self.rname + '\n' + self.rdescription