# Implement a class to hold room information. This should have name and
# description attributes.


from item import Item

class Room:
    def __init__(self, name, description):
        super().__init__()
        self.name = name
        self.description = description
        self.items = []
    
    def __str__(self):
        return f'{self.name} - {self.description}'
    
    def print_items(self):
        if len(self.items) > 0:
            print('items:\n')
            for i in self.items:
                print(f'{i.name} - {i.description}')
        else:
            print('no items')
            
    def search_items(self, item):
        for i in self.items:
            if i.name.lower() == item:
                return i
        else:   
            print('Item does not exist.')
            self.print_items()

    def add_item(self, item):
        self.items.append(item)

    def drop_item(self, item):
        self.items.remove(item)