# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
  def __init__(self, name, description):
    self.name = name,
    self.description = description

  def new_room(self, direction):
    if direction == 'n' and hasattr(self, 'n_to'):
      return self.n_to
    elif direction == 's' and hasattr(self, 's_to'):
      return self.s_to
    elif direction == 'w' and hasattr(self, 'w_to'):
      return self.w_to
    elif direction == 'e' and hasattr(self, 'e_to'):
      return self.e_to
    else:
      print('You can not go to that direction.')