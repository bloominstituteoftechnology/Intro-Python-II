import random
import time

import items


##### Player Setup #####
class Player:
  def __init__(self):
    self.name = ''
    self.type = ''
    self.health = 0
    self.armor = 0
    self.attack = 0
    self.experience = 0
    self.inventory = []
    self.status = []
    self.location = 'The Outskirts'
    self.isAlive = True

  def getName(self):
    return self.name
  def getType(self):
    return self.type
  def getHealth(self):
    return self.health
  def getArmor(self):
    return self.armor
  def getAttack(self):
    return self.attack
  def getExperience(self):
    return self.experience
  def getInventory(self):
    return self.inventory
  def getStatus(self):
    return self.status
  def getLocaltion(self):
    return self.location
  def getisAlive(self):
    return self.isAlive

  def setName(self, newName):
    self.name = newName
  def setType(self, newType):
    self.type = newType
  def setHealth(self, newHealth):
    self.health = newHealth
  def setArmor(self, newArmor):
    self.armor = newArmor
  def setAttack(self, newAttack):
    self.attack = newAttack
  def setExperience(self, newExperience):
    self.experience = newExperience
  def setInventory(self, newInventory):
    self.inventory = newInventory
  def setStatus(self, newStatus):
    self.status = newStatus
  def setLocation(self, newLocation):
    self.location = newLocation
  def setisAlive(self, newisAlive):
    self.isAlive = newisAlive

  def __str__(self):
      return "{}, {}, {}, {}, {}, {}, {}, {}, {}, {}\n".format(self.name, 
                                                              self.type,
                                                              self.health,
                                                              self.armor, 
                                                              self.attack,
                                                              self.experience,
                                                              self.inventory, 
                                                              self.status, 
                                                              self.location, 
                                                              self.isAlive
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

