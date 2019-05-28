# Write a class to hold player information, e.g. what room they are in
# currently.
from room import Room

class Player:
  def __init__(self, location, inventory=['empty']* 3):
    self.location = location
    self.inventory = inventory
  def moveTo(self, lst, key):
    new_location = [extension for extension in lst if(extension in key.name.lower())]
    self.location = new_location[0]
  def addTo(self, item):
    pass
