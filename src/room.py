# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name= 'Room', description= 'An Empty Room', items =[], n_to = 'Nowhere to go here!', s_to = 'Nowhere to go here!', e_to = 'Nowhere to go here!', w_to = 'Nowhere to go here!', rm_layout = 'o'):
        self.name = name
        self.description = description
        self.items = items
        self.n_to = n_to
        self.s_to = s_to
        self.e_to = e_to
        self.w_to = w_to
        self.rm_layout = rm_layout
    
    def add_item(self, item):
        self.items.append(item)
    def pickup_item(self, item):
        if item in self.items:
            self.items.remove(item)
        else:
            print("but I don't see any....")

    def __str__(self):
        return f'{self.name} \n-----\n{self.rm_layout} \n-----\n{self.description}'
    
    def __repr__(self):
        return f'Room({self.name}, {self.description}, {self.n_to}, {self.s_to}, {self.e_to}, {self.w_to})'

#testRoom = Room('Test', s_to = 'Disneyland!!')
#print(testRoom)
#print(repr(testRoom))