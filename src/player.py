from container import Container

class Player(Container):
  def __init__(self, room, items = None):
    super().__init__(items)

    self.room = room

  def __str__(self):
    s = "Location\n"+str(self.room) + "\n"
    s = s + "\nInventory:\n" + "\n".join([str(i) for i in self.items])
    return s