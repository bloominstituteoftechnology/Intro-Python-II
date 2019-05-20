import items
import winsound
# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
  def __init__(self, name, room, inventory=[]):
    self.name = name
    self.room = room
    self.inventory = ["Gold"]
 # def __repr__(self):
    

  def print_inventory(self):
    for item in self.inventory:
      print(item)
    
  def play_audio(self, snd_file): 
    winsound.SND_FILENAME = snd_file
    winsound.PlaySound(winsound.SND_FILENAME, winsound.SND_ASYNC)               
    