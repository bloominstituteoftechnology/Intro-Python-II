class Item:
    def __init__(self, items_name = None, item_description =None):
        if items_name is None:
           self.items_name = []
        else:
            self.items_name= items_name
        self.item_description = item_description




items= Item('sword', 'Be carefull') 
#print (item_1.items_name)     