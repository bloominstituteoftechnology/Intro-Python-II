# Implement a class to hold room information. This should have name and
# description attributes.
from item import Item
class Room:
    def __init__(self,name,description,n_to, s_to, e_to, w_to):
       self.name=name
       self.description= description
       self.n_to =n_to
       self.s_to = s_to
       self.e_to = e_to
       self.w_to = w_to
       self.items=[]

    def getItems(self):
        return self.items

    def add_item(self,item):
        return self.items.append(item)

    def delete_item(self,item):
        return self.items.remove(item)

    def __repr__ (self):
        return "Name : " + self.name + " \n Description :"  + self.description +"\n Items in the room : " + str(self.items)
