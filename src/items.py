
   
class Item():
  def __init__(self, name):
    self.name = name
   
  def __str__(self):
    return "{}\n".format(self.name)


class Weapon(Item):
    def __init__(self, name):
        super().__init__(name)

    def __str__(self):
        return "{}\n".format(self.name)

class Gold(Item):
    def __init__(self, name):
        super().__init__(self.name)