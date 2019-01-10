# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
  def __init__(self, name, current_room):
    self.name = name
    self.current_room = current_room

  def move(self, room):
    if room:
      self.current_room = self.current_room.new_room(room)
    else:
      print('You can not go that way')