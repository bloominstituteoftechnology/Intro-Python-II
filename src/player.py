# Write a class to hold player information, e.g. what room they are in
# currently.
from room import Room

class Player(Room):
  def __init__(self, name, job, race, stats, inventory):
    self.name = name
    self.job = job
    self.race = race
    self.stats = stats
    self.invetory = inventory
    Room.__init__(self, "outside", "North of you, the cave mount beckons")
  def currentRoom(self):
    return '\nYou are currently: ' + self.rname + '\n' + self.rdescription+'\n'