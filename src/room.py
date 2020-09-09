# Implement a class to hold room information. This should have name and description attributes.

class Room:
  def __init__(self, name, description):
    self.name = name
    self.description = description

  def get_direction(self, direction):
    if direction == "n":
      print("Moving North")
      return self.n_to
    elif direction == "s":
      print("Moving South")
      return self.s_to
    elif direction == "e":
      print("Moving East")
      return self.e_to
    elif direction == "w":
      print("Moving West")
      return self.w_to
    else:
      print("Invalid Direction")
      return None