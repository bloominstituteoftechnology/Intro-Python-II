class Item:
   def __init__(self, name, description):
      self.name = name
      self.description = description

   def on_take(self, item):
      print(f"You have picked up {item}")

   def on_drop(self, item):
      print(f"You have picked up {item}")

   def __repr__(self):
      return self.name