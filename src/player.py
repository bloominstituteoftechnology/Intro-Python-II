import items, monsters
import winsound
# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
  def __init__(self, name, room, hp=100, damage=25, inventory=[]):
    self.name = name
    self.room = room
    self.hp = hp
    self.damage = damage
    self.inventory = ["Gold"]
 # def __repr__(self):
    

  def print_inventory(self):
    for item in self.inventory:
      print(item)
    
  def play_audio(self, snd_file): 
    winsound.SND_FILENAME = snd_file
    winsound.PlaySound(winsound.SND_FILENAME, winsound.SND_ASYNC) 

  def am_alive(self):
    if self.hp > 0:
      return True

  def attack(self, monster, hp, damage):
    if self.am_alive():
      if self.room.monster:
        hp -= self.damage
        if hp > 0:
          self.play_audio("01_Hammer.wav")
          print("You attacked monster, it's hp is now:" + str(hp))
        else:    
          self.room.monster.pop()
          print("Monster is dead...")
          return        

        self.hp -= damage
        if self.am_alive():
          print("Monster attacked, your hp is now: " + str(self.hp))
        else:
          print("Monster killed you dead...")
          
