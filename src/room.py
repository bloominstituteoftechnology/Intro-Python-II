# Implement a class to hold room information. This should have name and
# description attributes.

from item import Item



class Room:
    def __init__(self, name, description, n_to = 0, s_to = 0, e_to = 0, w_to = 0):
    

        self.name = name
        self.description = description
        self.n_to = n_to
        self.s_to = s_to
        self.e_to = e_to
        self.w_to = w_to
        self.items =  []
      

    def __str__(self) :
        

        s = f'{self.name} {self.description} '  
        return s

    def add_item(self, item):
        self.items.append(item)

    def print_item(self):
        print('The items in this room:')
        if self.items != None:
            for i in self.items:
                print(i)
    
    def remove_item(self,item):
        self.items.remove(item)