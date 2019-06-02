# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
  def __init__(self, name, current_room_name, items=None):
    self.name = name
    self.current_room_name = current_room_name
    if items is None:
      self.items = []
    else:
      self.items = items  

  def __str__(self):
    return f"{self.name} you are in {self.current_room_name} room."

