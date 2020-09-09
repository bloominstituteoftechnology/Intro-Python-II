# Write a class to hold player information, e.g. what room they are in currently.

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
    # TODO: take away item from room
    print(f"Picked up {item} in {room}")
