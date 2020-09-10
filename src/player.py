# Write a class to hold player information, e.g. what room they are in currently.
from room import Room

class Player:
  def __init__(self, name, current_room):
    self.name = name
    self.current_room = current_room
    self.items = []

  def move(self, direction):
    next_room = self.current_room.get_direction(direction)
    if next_room is not None:
      self.current_room = next_room
    else:
      print("You bumped into a wall")

  def take_item(self, item, room):
    self.items.append(item)
    print("-------------------------------------------------------")
    print(f"*Picked up {item.name} in {room}.")

  def drop_item(self, item):
    self.items.remove(item)
    self.current_room.add_item(item)
    print("-------------------------------------------------------")
    print(f"*Dropped {item.name}.")

  def show_inventory(self):
    print("-------------------------------------------------------")
    print("Inventory:")
    if len(self.items) == 0:
      print("empty")
    for item in self.items:
      print(f"  {item.name}")
    #print("")
