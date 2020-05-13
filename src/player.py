# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
  def __init__(self, name, room):
    self.name = name
    self.currentroom = room

  def move_to(self, room):
    self.currentroom = room
    print(f'\n{self.name} moved to {room.name}.\n')