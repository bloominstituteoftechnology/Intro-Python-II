# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, name, description, items = []):
        self.name = name
        self.description = description
        self.n_to = ""
        self.e_to = ""
        self.s_to = ""
        self.w_to = ""
        self.items = items
        

    def print_room_info(self):
        print(f'\n{self.name}\n\n{self.description}\n')

    def room_items(self):
        if len(self.items) > 0:
            print(f'This room contains the following items:')
            for i in self.items:
                print(f'{i.name}: {i.description}')
        else:
            print('No items available in this room')

    def get_item(self, item):
        for i in self.items:
            if(i.name.lower() == item.lower()):
                return(i)         

    def remove_item(self, item):
        for i in self.items:
            if(i.name.lower() == item.lower()):
                self.items.remove(i) 
                print(f"\nYou have picked up: {i.name}")