import random
import time

import items


##### Player Setup #####
class Player():
  def __init__(self):
    self._name = "None"
    self._archetype = "None"
    self._health = 0
    self._armor = 0
    self._attack = 0
    self._experience = 0
    self._inventory = []
    self._status = []
    self._location = "None"
    self._isAlive = True

  @property
  def name(self):
    return self._name
  @property
  def archetype(self):
    return self._archetype
  @property
  def health(self):
    return self._health
  @property
  def armor(self):
    return self._armor
  @property
  def attack(self):
    return self._attack
  @property
  def experience(self):
    return self._experience
  @property
  def inventory(self):
    return self._inventory
  @property
  def status(self):
    return self._status
  @property
  def location(self):
    return self._location
  @property
  def isAlive(self):
    return self._isAlive
  
  @name.setter
  def name(self, x):
    self._name = x
  @archetype.setter
  def archetype(self, x):
    self._archetype = x
  @health.setter
  def health(self, x):
    self._health = x
  @armor.setter
  def armor(self, x):
    self._armor = x
  @attack.setter
  def attack(self, x):
    self._attack = x
  @experience.setter
  def experience(self, x):
    self._experience = x
  @inventory.setter
  def inventory(self, x):
    self._inventory = x
  @status.setter
  def status(self, x):
    self._status = x
  @location.setter
  def location(self, x):
    self._location = x
  @isAlive.setter
  def isAlive(self, x):
    self._isAlive = x

  def __str__(self):
      return "0/{},1/{},2/{},3/{},4/{},5/{},6/{},7/{},8/{},9/{}\n".format(
        self.name, self.archetype, self.health, self.armor,  self.attack, 
        self.experience, self.inventory, self.status, self.location, self.isAlive
      )

##### Inventory Setup #####
# def get_item(self, item):
#     if item in self.current_room.items:
#         self.current_room.items.remove(item)
#         self.items.append(item)
#         item.on_take()
#     else:
#         print(f"There is no {item.name.lower()}")


# def drop_item(self, item):
#     if item in self.items:
#         self.items.remove(item)
#         self.current_room.items.append(item)
#         item.on_drop()
#     else:
#         print(f"{item.name} is not in your inventory.")


# def print_items(self):
#     if len(self.items) > 0:
#         item_list = "You are holding the following items:"
#         for item in self.items:
#             item_list += f"\n\t-{item}"
#     else:
#         item_list = "You are not holding anything"
#     print(item_list)


# myPlayer = Player()

if __name__ == "__main__":
  ##### Class Declaration ######
  myPlayer = Player()
  print(myPlayer)
  
  #> Reference
  # myPlayer.name=""
  