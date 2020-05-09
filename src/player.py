# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
   def __init__(self, player_name, curr_location, items_found-[]):
      self.player_name = player_name
      self.curr_location = curr_location
      self.items_found = items_found
      
   def get_inventory(self):
      return self.items_found
   
   def __str__(self):
      return str(self.__dict__)   