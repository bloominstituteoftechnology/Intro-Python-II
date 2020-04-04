from container import Container

class Player(Container):
  def __init__(self, name, current_room, items = None):
    super().__init__(items)

    self.name = name
    self.current_room  = current_room 

  def __str__(self):
    s = "Location\n"+str(self.current_room ) + "\n"
    s = s + "\nInventory:\n" + "\n".join([str(i) for i in self.items])
    return s