from item import Inventory

class Player:
  def __init__(self, name, current_room, items):
    self.name = name
    self.current_room = current_room
    self.items = items

  def __str__(self):
    return f"{self.name}, {self.current_room}, {self.items}"

  def action_input(self, decision):
    if decision == 'n':
      if self.current_room.n_to is not None:
          self.current_room = self.current_room.n_to
    elif decision == 's':
      if self.current_room.s_to is not None:
        self.current_room = self.current_room.s_to
    elif decision == 'e':
      if self.current_room.e_to is not None:
        self.current_room = self.current_room.e_to
    elif decision == 'w':
      if self.current_room.w_to is not None:
        self.current_room = self.current_room.w_to
    elif decision == 'i':
      self.items.show_inventory()
    else:
      print("Thank you for playing")

  def display_room(self):
    print(f'Current Room: {self.current_room.name}\n \n{self.current_room.description}\n \n{self.current_room.room_items()} ')

class PlayerInventory(Inventory):
  def __init__(self, items):
    super().__init__(items)

  def drop_item(self, remove):
    if self.items is not None and remove in self.items.keys():
      print(f'You dropped {remove}')
      self.items.pop(remove)
      return self.items
    else:
      print('You possess no such items to drop.\n')

  def show_inventory(self):
    parent_show = super().show_inventory
    parent_show()
    invent_check = input("Choose an action: Drop Item(d), Back(b): \n")
    
    if invent_check == 'd':
      remove = input("which item would you like to drop?: ")
      self.drop_item(remove.lower())