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
            if (i.name.lower() == item.lower()):
                self.items.remove(i)
                print(f'\n{"*" * 58}\n')  
                print(f"You have picked up: {i.name}".center(58, ' '))
                return(i)
                break
        else: 
            print(f'\n{"*" * 58}\n')  
            print(f"Make sure the item is available".center(58, ' '))             

    def add_item(self, item):
        self.items.append(item)
        print(f'\n{"*" * 58}\n') 
        print(f"You have dropped: {item.name}".center(58, ' '))