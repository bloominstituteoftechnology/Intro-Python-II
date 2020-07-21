

class Item: 
    def __init__(self, item_name, item_description):
        self.item_name = item_name 
        self.item_description = item_description

    def __repr__(self):
        return(f'{self.item_name}, {self.item_description}')