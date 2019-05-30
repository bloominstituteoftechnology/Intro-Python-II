# Implement a class to hold room information. This should have name and
# description attributes.

class Room():
   def __init__(self, name, description):
      self.name = name
      self.description = description

   def change_name(self, new_name):
      self.name = new_name

   def change_description(self, new_description):
      self.description = new_description

   def __repr__(self):
      return f"{self.name}"