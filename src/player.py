# Write a class to hold player information, e.g. what room they are in
# currently.

class Player():
   def __init__(self, name, room, inventory=[]):
      self.name = name
      self.current_room = room
      self.inventory = inventory

   def __repr__(self):
      return f"{self.name} is currently in the {self.current_room}"