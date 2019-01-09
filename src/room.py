# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
  def __init__ (self, name, description, items) :
    self.name = name
    self.description = description
    self.items = items

dasroom = Room("Livingroom", "the room of living", ['item1', 'item2'])

print(dasroom.items)
