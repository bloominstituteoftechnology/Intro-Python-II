class Item():
  def __init__(self, name, description):
    self.name = name
    self.description = description

  def __repr__(self):
    return "\n{}: {}\n".format(self.name, self.description)

  def get_name(self):
    return self.name

  def get_description(self):
    return self.description
