# Write a class to hold player information, e.g. what room they are in
# currently.
from item import Item

class Player:
  def __init__(self, name, current_room):
    self.name = name
    self.current_room = current_room
    self.inventory = [Item("weapons")] 

  def show_items(self):
    result = str(self.name) + ' you have the following items>>> \n'
    for item in self.inventory:
      result += str(item) + "\n"
    print(result)    

  def add_items(self,new_item):
    self.inventory.append(new_item)
    self.show_items()   

  def delete_items(self, item_remove):
    if (item_remove in self.inventory):
      self.inventory.remove(item_remove)
      self.show_items()
    else:
      print("You do not that item to remove")  


  def __str__(self):
    return f"{self.name} you are at >>> {self.current_room.name} room."

