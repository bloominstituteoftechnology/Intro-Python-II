# Write a class to hold player information, e.g. what room they are in
# currently.

class Player():
   def __init__(self, name, room):
      self.name = name
      self.current_room = room

   def change_name(self, name):
      self.name = name
   def move_room(self, new_room):
      self.current_room = new_room

   def __str__(self):
      return f"{self.name} is currently in the {self.current_room}"