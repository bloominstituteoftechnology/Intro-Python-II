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
    if new_item in self.inventory:
      print("Item already exits. Duplicates are not allowed.")       
    else:
      self.inventory.append(new_item)
      self.show_items() 
      
  def get_item(self, which_item):
    arr = self.inventory
    find = False
    for item in arr:
      if item == which_item:
        find = True
        # print(self.name + "Here is the item you are looking for " + item)
    if find:
      print(self.name + " here is the item you are looking for " + item)
    else:
      print(self.name + " There is no such a item in the list.")   

  def delete_items(self, item_remove):
    if (item_remove in self.inventory):
      self.inventory.remove(item_remove)
      print(self.name+ " you have deleted " + item_remove)
      self.show_items()
    else:
      print("You do not that item to remove")  


  def __str__(self):
    return f"{self.name} you are at >>> {self.current_room.name} room."

