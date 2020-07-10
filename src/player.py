# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
  def __init__(self, name, location):
    self.name = name[0].upper() + name[1:]
    self.location = location
    self.inventory = {}

# ---------------------------------------------------------------------------Movement

  def move(self):
    directionOption = ['south', 'north', 'west', 'east' , 'n', 'w', ]    
    direction = input('Which direction would '+ self.name + ' like to go? \n')
    room = self.location

    if direction.lower() in directionOption:      
      directionKey = direction[0] + '_to'
      try:
        self.location = room.nextRoom(directionKey)
      except AttributeError:
        print(f'\nYou turn {direction} and see no path. You remain where you are.\n')

    else:
      print(f'invaild direction. Please pick one of the following. {directionOption}')

# -------------------------------------------------------------------------- Items      
  
  def checkInventory(self):
      print(f'You have {len(self.inventory)} items')
      # if len(self.inventory) == 1: # FOR WHEN A PLAYER ONLY HAS ONE ITEM
      #   item = self.inventory[0]    
      #   self.checkItem(item)        
      
      if len(self.inventory) > 0: # FOR WHEN A PLAYER HAS MORE THAN ONE ITEM
        item = self.chooseItemFromInventory() # PICKS AN ITEM FROM THE INVENTORY
        if item:
          self.checkItem(item) # CHECKS ITEM
        else:
          print('item does not exist')
          self.chooseItemFromInventory() 



  def chooseItemFromInventory(self):
    items = [item for item in self.inventory]
    print('Inventory:')
    for item in items:
      print(item)

    choice = input('Pick an item.')

    if choice.lower() in items:
      return self.inventory[choice]
      
    else:
      return ''     

  def checkItem(self, item):  
    choice = input('Would you like to get a closer look at ' + item.name + '. \n y/n') # ASKS IF USER WANTS TO READ ITEM DESCRIPTION
    if choice[0].lower() == 'y':  
      item.readDescription()
      choice = input('What would you like to do with this item?\nd(Drop) || u(Use)')  # ASKS WHAT THE PLAYER WANTS TO DO WITH ITEM(S)
      if choice[0].lower() == 'd': # DROPS ITEM
        self.dropItem(item)
      if choice[0].lower() == 'u': # USES ITEM
        item.useItem()

  def dropItem(self, item):
    self.location.additem(item) 
    del self.inventory[item.name]

  def checkRoom(self):    
    room = self.location
    items = [item for item in room.items.values()]

    print(f'There are {len(items)} item(s) in this Room.')
    if len(items) < 1:
      print('\nYou turn your attention back to the room\n')     

    else:
      print(items)
      for item in items:
        print(item.name)

      choice = input("Which one would you like to pick up?")

      if choice in room.items:
        item = room.items[choice]
        room.removeItem(choice)
        self.inventory[choice] = item
      else:
        print('Item not found. Please try again.')
        self.checkRoom()