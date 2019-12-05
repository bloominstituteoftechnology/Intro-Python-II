class Item():
    ''' base class goes here'''
    def __inti__(self, name, description):
        self.name = name
        self.description = description
        
    def __str__(self):
        return f'{self.name} is  {self.description}.'