from container import Container

class Room(Container):
  def __init__(self, name, description, items = None, n_to = None, s_to = None, e_to = None, w_to = None):
    super().__init__(items)
    self.name = name
    self.description = description

    self.n_to = n_to
    self.s_to = s_to
    self.e_to = e_to
    self.w_to = w_to

  def __str__(self):
    s = self.name + ":\n  " + self.description + "\n"
    s = s + "\n".join([str(i) for i in self.items])
    return s