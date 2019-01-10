class Item:
  def __init__(self, name, desciption):
    self.name = name
    self.desciption = desciption

  def __repr__(self):
    return f'This is the item {self.name}'