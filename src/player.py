# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
  def __init__(self, name, currentRoom, items=[]):
    self.name = name
    self.currentRoom = currentRoom
    self.items = items

