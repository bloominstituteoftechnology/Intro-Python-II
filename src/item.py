class Item:
  def __init__(self, name, description):
    self.name = name
    self.description = description

  def __str__(self):
    return f"{self.name} : {self.description}"
    # return f'{{"{self.name}": "{self.description}"}}'
  
  def see_item(self):
    # return f'{{"{self.name}": "{self.description}"}}'
    yup = {self.name: self.description}
    return yup


class Inventory:
  def __init__(self, items = None):
    self.items = items

  def __str__(self):
    if self.items is not None:
      print(f"There are {int(len(self.items))} item(s) in your inventory.\n")
      count = 0
      for name, description in self.items.items():
        if int(count) < int(len(self.items))-1: 
          print(f"{name}: {description}, ", end ='')
          count += 1
        elif int(count) == int(len(self.items))-1:
          print(f"and {name}: {description}")
    else:
      print("There are no items in your inventory.")

  def add_item(self, add):
    # print(add)
    # self.items = add
    if self.items is not None:
      test = self.items
    else:
      test = {}
    for name, description in add.items():
      new = Item(name, description).see_item()
      test.update(new)
    self.items = test
    print(self.items)
      

more_items={'cat': "cute", 'dog': "poop"}
test = Inventory()

print(test.add_item(more_items))
print(test.add_item({'yup': 'hi'}))

# test.add_item(more_items)

# print(test)  inventory has items Associative / rock is an item inheritance / items[rock.name]