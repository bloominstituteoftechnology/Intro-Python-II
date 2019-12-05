# Implement a class to hold room information. This should have name and
# description attributes.

class Room():
    ''' class for room'''
    def __init__(self, description, room):
        self.room = room 
        self.description = description
        self.items = []
        self.n_to = None
        self.w_to = None
        self.e_to = None
        self.s_to = None
    #direction attr should point to room in that direction, when added causes err
    def __str__(self):
       self_items = f' This is {self.room}: {self.description}. Look I found a {self.items}'
       for x in self_items:
           self_items += f'{x}'
           print('self items', x)
           return self_items


