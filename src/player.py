# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
  def __init__(self, name, location):
    self.name = name[0].upper() + name[1:]
    self.location = location

  def move(self, room):
    directionOption = ['south', 'north', 'west', 'east']    
    direction = input('Which direction would '+ self.name + ' like to go? \n')

    if direction.lower() in directionOption:      
      directionKey = direction[0] + '_to'
      try:
        self.location = room.nextRoom(directionKey)
      except AttributeError:
        print(f'\nYou turn {direction} and see no path. You remain where you are.\n')



    else:
      print(f'invaild direction. Please pick one of the following. {directionOption}')
    
