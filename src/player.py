#>
#> Main file
#>
import random
import time

import world as wrld
import items as itms

##### Player Setup #####
class Player():
  """Parent player class"""
  def __init__(self):
    self._name = ""
    self._archetype = ""
    self._health = 0
    self._armor = 0
    self._attack = 0
    self._experience = 0
    self._inventory = []
    self._status = []
    self._location = wrld.dictWorld['theOutskirts']
    self._isAlive = True

  # def playerMovement(self, location):
  #   if direction == None:
  #     print("There is nothing here.")
    
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


# def movementDev_loop():
#   print("\nMovementDev [1] North  [2] South")
#   user_InputDev = input("> ")
  
#   while user_InputDev not in ["1", "2"]:
#     print('Invalid input...')
#     print("\nMovementDev [1] North  [2] South")
#     user_InputDev = input("> ")
    
#   if user_InputDev == "1":
#       if myPlayer.location._north == None:
#         print("There seems to be nothing of interest North of here.")
#         movementDev_loop()
#       else:
#         print(myPlayer._location)
#         myPlayer.location = myPlayer.location._north
#         print(myPlayer._location)
#         print(f"You've reached {myPlayer.location._name}, we should continue...")
#         movementDev_loop()
#   elif user_InputDev == "2":
#       if myPlayer.location._south == None:
#         print("There seems to be nothing of interest South of here.")
#         movementDev_loop()
#       else:
#         myPlayer.location = myPlayer.location._south
#         print(f"You've reached {myPlayer.location._name}, we should continue...")
#         movementDev_loop()
#   print('Done!')





# def lineClear(n):
#   if n % 2 == 0:
#     sys.stdout.write("\033[F"*(n+3))
#     print('\n                                                                    '*(n+3))
#     sys.stdout.write("\033[F"*((n+3)//2))
  # else: # n % 2 != 0:
  #   pass




if __name__ == "__main__":
  ##### Movement check #####
  
  myPlayer = Player()
  myPlayer.inventory = [Torch(), Silver(15)]

  def introPlayer():
    return myPlayer._location._intro()


  def movementDev_loop():
    print("MovementDev [1] North  [2] South\n")
    user_InputDev = input("> ")

    while user_InputDev not in ["1", "2"]:
      print('\nInvalid input...\n')
      time.sleep(1)
      print("MovementDev [1] North  [2] South\n")
      user_InputDev = input("> ")
    if user_InputDev == "1":
      if myPlayer.location._north == None:
        print_pause("Dev_There is nothing North of here.", postpause=1)
        movementDev_loop()
      else:
        myPlayer._location = dictWorld[myPlayer._location._north]
        if myPlayer._location._explored == True:
          print_pause(f"You've reached {myPlayer.location._name}, we should continue...")
          time.sleep(1)
          movementDev_loop()
        elif myPlayer._location._explored == False:
          myPlayer._location._explored = True
          introPlayer()
          time.sleep(1)
          # def print_pauseUpdate(line, name=None, pause=0.02, postpause=1, initIndent='', subIndent='', n=False):          
          stringLine = f"You've reached {myPlayer.location._name}, we should continue..."
          print_pauseUpdate(stringLine, initIndent=1)
          # sys.stdout.write("\033[F"*1) 
          # print(' '*30)
          # sys.stdout.write("\033[F"*3) 
          movementDev_loop()
    if user_InputDev == "2":
      if myPlayer.location._south == None:
        print("Dev_There is nothing South of here.")
        time.sleep(1)
        movementDev_loop()
      else:
        myPlayer._location = dictWorld[myPlayer._location._south]
        if myPlayer._location._explored == True:
          print_pause(f"You've reached {myPlayer.location._name}, we should continue...")
          time.sleep(1)
          movementDev_loop()
        elif myPlayer._location._explored == False:
          myPlayer._location._explored = True
          introPlayer()
          time.sleep(1)
          print_pause(f"You've reached {myPlayer.location._name}, we should continue...")
          
  # sys.stdout.write("\033[F"*28)        
  movementDev_loop()
          
        
  # print(myPlayer._location)
  # myPlayer._location = dictWorld[myPlayer._location._north]
  # print('\n')
  # print(myPlayer._location._explored)
  # myPlayer._location._explored = True
  # print(myPlayer._location._explored)
  # print('\n')
  # print(myPlayer._location)
  # print('\n')
  # myPlayer._location = dictWorld[myPlayer._location._south]
  # print('\n')
  # print(myPlayer._location)
  # print(myPlayer._location._explored)
  # print('\n')
  # myPlayer._location = dictWorld[myPlayer._location._north]
  # print('\n')
  # print(myPlayer._location)
  # print(myPlayer._location._explored)
        
  # movementDev_loop()
    
#   if user_InputDev == "1":
#       if myPlayer.location._north == None:
#         print("There seems to be nothing of interest North of here.")
#         movementDev_loop()
#       else:
#         print(myPlayer._location)
#         myPlayer.location = myPlayer.location._north
#         print(myPlayer._location)
#         print(f"You've reached {myPlayer.location._name}, we should continue...")
#         movementDev_loop()
#   elif user_InputDev == "2":
#       if myPlayer.location._south == None:
#         print("There seems to be nothing of interest South of here.")
#         movementDev_loop()
#       else:
#         myPlayer.location = myPlayer.location._south
#         print(f"You've reached {myPlayer.location._name}, we should continue...")
#         movementDev_loop()
#   print('Done!')
  
  
  
  
  # print('myPlayer.location.__contains__(north)')






  # myPlayer.inventory = [items.Torch(), items.Silver(15)]
  # for attr in ['name', 'description']:
  #   print(getattr(myPlayer.inventory[0], attr))
  # myPlayer.location = world.theOutskirts