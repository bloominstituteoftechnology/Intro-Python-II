# Implement a class to hold room information. This should have name and
# description attributes.
from item import Item
class Room:
    def __init__(self, name, description = ''):
        self.name = name
        self.description = description
        self.n_to = self
        self.s_to = self
        self.w_to = self
        self.e_to = self
        self.items = []
    
    # str() method returns room name, desc, and current items
    def __str__(self):
        output = f'You are now in the {self.name} \n {self.description} \n'
        for i, c  in enumerate(self.items):
            output += "Items: " + str(i+1) + ". " + c.name + "\n"
        return output

    def __repr__(self):
        return '{ room: ' + self.name + ' n_to: ' + self.n_to.name + ' s_to: ' + self.s_to.name + ' e_to: ' + self.e_to.name + ' w_to: ' + self.w_to.name + ' }'
    
    # # abtract away current_room = current_room.n_to
    def move(self, direction):
        direction = direction + "_to"
        new = self.__getattribute__(direction)
        if new == self:
            print("There is nothing there.")
        else:
            print(new)
        return new

    # returns a list of directions you can move in 
    def possible_directions(self):
        directions = {}
        directions.update({ 'n': self.n_to, 's': self.s_to, 'w': self.w_to, 'e': self.e_to})
        print(self)
        msg = f'You choices are: '
        for d, r in dict(directions).items():
            if  r is self:
                del directions[d]
            if r != self:
                msg += d + " "
        print(msg)
        return list(directions.values())
    
    # method for addding items to room
    def add_item_to_room(self, name, desc):
        item = Item(name, desc)
        self.items.append(item)

    # returns a list of item names that are in the room
    def list_items(self):
        names= []
        for item in self.items:
            names.append(item.name)
        return names


    def hasitem(self, item_name):
        return item_name in self.list_items()
    
    
    # example getters and setters
    def set_descrip(self, room_description):
        self.description = room_description

    def get_descrip(self):
        return self.description