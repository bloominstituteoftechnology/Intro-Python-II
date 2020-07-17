# Implement a class to hold room information. This should have name and
# description attributes.
from item import Item

class Room: 
        # instance attributes... will vary 
        def __init__(self, name, description, items, item_name, item_description):
            super().__init__(item_name, item_description)
            self.name = name
            self.description = description
            self.items = items
            
        # add list of [items]

    # ['Teddy bear', ['pencil', 'A mighty pencil for drawing'], ['poster',' A Poster of MJ']]

  
     
      
