# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
  def __init__ (self, name, room) :
    self.name = name
    self.room = room

player1 = Player('John Snow', 'beyondthewall')

print(player1.name)