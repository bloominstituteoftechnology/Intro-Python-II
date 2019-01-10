# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
  def __init__(self, currentLocation):
    self.currentLocation = currentLocation

  def __repr__(self):
    return f'Player is in {self.currentLocation}'

  def moveTo(self, newLocation):
    self.currentLocation = newLocation