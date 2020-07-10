class Item:
  def __init__(self, name, description):
    self.name = name
    self.description = description

  # def __repr__(self):
  #   return f'{self.name}'  
    
  def readDescription(self):
    print(f'{self.description}')
  
  def useItem(self):
    print(self.name + 'can not be used')
      