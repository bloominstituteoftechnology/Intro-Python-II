# Write a class to hold player information, e.g. what room they are in
# currently.

class Player(Room):
  def __init__ (self, name, room, bag) :
    self.name = name
    self.room = room
    self.bag = bag
  super().__init__(self)
player1 = Player("John Snow", "beyondthewall", [])

print(player1.name)