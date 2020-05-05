# Write a class to hold player information, e.g. what room they are in
# currently.

class Player():
  def __init__(self, start, name):
    self.current_room = start
    self.name = name
    self.items = []
    self.item_names = []
