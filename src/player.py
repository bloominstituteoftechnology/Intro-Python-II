# Write a class to hold player information, e.g. what room they are in
# currently.
#from room import Room

class Player():
  def __init__(self, name, job, race, stats, inventory, Room):
    self.name = name
    self.job = job
    self.race = race
    self.stats = stats
    self.inventory = inventory
    self.Room = Room
  def currentRoom(self):
    return '\n' + self.name + ', the ' + self.race + ' ' + self.job + ', stands near the... ' + self.Room.name + '\n~' + self.Room.description + '~\n'
  def addItem(self, item):
    self.inventory.append(item)
  def removeItem(self, item):
    try:
      self.inventory.remove(item)
      return True
    except ValueError:
      return False