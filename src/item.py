from room import Room
# an item is a child to Room class because rooms can have multi items 
class Item(Room): 
    def __init__(self, name, description, title, weight):
        super().__init__(name, description)
        self.title = title 
        self.weight = weight
        
    def __str__(self):
        return super(Item, self).__str__() + f'testing, weight {self.weight} and title {self.title}'
    
    
    # local testing
test = Item('9.3lb', 'volleyball')
print(super(Item, test).__str__())
print(test)
    
    # global testing 
# print(super(Item, test).__str__())
   