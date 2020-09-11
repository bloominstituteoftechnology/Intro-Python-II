from player import Player
from room import Room
import random

class Enemy:
  def __init__(self, name, hp, atk):
    self.name = name
    self.hp = hp
    self.atk = atk

  def __str__(self):
    return f"[{self.name}] - HP: {self.hp}, ATK: {self.atk}"

  def attack(self, player: Player):
    attack_chance = random.randint(1, 3)
    print("-------------------------------------------------------")
    print(f"{self.name} attacked!")
    if attack_chance != 1:
      print("HIT!")
      player.hp -= self.atk
      print(f"{player.name} now has {player.hp} HP")
      print("-------------------------------------------------------")
    else:
      print("MISS")
      print("-------------------------------------------------------")

room = Room("hallway", "sdf")
player = Player("Matt", room, 300, 100)

ogre = Enemy("Ogre", 200, 50)
