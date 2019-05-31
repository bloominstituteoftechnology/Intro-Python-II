# Implement a class to hold room information. This should have name and
# description attributes.

class Room():
   def __init__(self, name, description, items=[]):
      self.name = name
      self.description = description
      self.items = items

   def add_item(self, item):
      self.items.append(item)

   def display_items(self):
      if len(self.items) == 0:
         return None
      else:
         for i in self.items:
            print(f"{i.name}")

   def __repr__(self):
      return f"{self.name}"