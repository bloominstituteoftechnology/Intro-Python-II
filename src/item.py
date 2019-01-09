class Item:
  def __init__ (self, name, description) :
    self.name = name
    self.description = description

item = Item("pen", "writey thingy")

print(item.name)