# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
   def __init__(self, name, room_desc, rm_items=[]):
      self.name = name
      self.room_desc = room_desc
      self.rm_items = rm_items
      
   def __str__(self):
      return str(self.__dict__   