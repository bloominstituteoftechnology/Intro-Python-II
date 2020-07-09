class Container():
  """ A generic class which can hold a list of items.
  """ 
  def __init__(self, items = None):
    if not items:
      self.items = []
    else:
      self.items = items