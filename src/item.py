class Item:                                 # Item Class takes in 2 arguments (name, description)
  def __init__(self, name, description):
    self.name = name
    self.description = description

  def __str__(self):
    return f"{self.name} : {self.description}"
    # return f'{{"{self.name}": "{self.description}"}}'
  
  def see_item(self):
    # return f'{{"{self.name}": "{self.description}"}}'
    return {self.name: self.description}


class Inventory:                            # Inventory Class takes in a dictionary of {name: description}
  def __init__(self, items = None):
    self.items = items

  def __str__(self):
    if self.items is not None:
      print(f"There are {int(len(self.items))} item(s).\n")
      count = 0
      for name, description in self.items.items():
        if int(count) < int(len(self.items))-1: 
          print(f"{name}: {description}, ", end ='')
          count += 1
        elif int(count) == int(len(self.items))-1:
          print(f"and {name}: {description}")
    else:
      print("There are no items.")

  def add_item(self, add):
    if self.items is not None:
      added = self.items
    else:
      added = {}
    for name, description in add.items():
      new = Item(name, description).see_item()
      added.update(new)
    self.items = added
    return(self.items)

  def drop_item(self, remove):
    if remove in self.items.keys():
      print(f'You dropped {remove}')
      self.items.pop(remove)
      return self.items
    else:
      print('No such items to drop.')

  def show_inventory(self):
    if self.items is not None:
      print(f"There are {int(len(self.items))} item(s).\n")
      count = 0
      inventory_list = {}

      for name, description in self.items.items():
        if int(count) < int(len(self.items))-1: 
          inventory_list.update(f"{name}: {description}, ", end ='')
          count += 1
        elif int(count) == int(len(self.items))-1:
          inventory_list.update(f"and {name}: {description}")
          return inventory_list
    else:
      return "There are no items."


more_items={'cat': "cute", 'dog': "poop"}
test = Inventory()
new_item = Item('boots','Are made for walking and that is what there will do.')
# print(new_item.see_item())
print(test.add_item(more_items))
print(test.add_item({'bow': 'Long and light; Easy to carry'}))
print(test.drop_item('bow')) 


# test.add_item(more_items)

# print(test)  inventory has items Associative / rock is an item inheritance / items[rock.name]