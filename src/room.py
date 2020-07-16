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

    def __str__(self) :
        

        s = f'{self.name} {self.description} '  
        return s

    # def add_items(self, item):
    #     self.items.append(item)

    # def print_item(self, item):

    #     if len(self.items >0):
    #         for i in item:
    #             print('The items in this room:')
    #             print(i)
    #     else:
    #         print('There are No Items In this Room.')      