# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.w_to = None
        self.e_to = None
        self.items = []
        
    def __str__(self):
        output = f'You are now in the {self.name} \n {self.description} \n'
        for i, c  in enumerate(self.items):
            output += "Items: " + str(i+1) + ". " + c.name + "\n"
        return output

    def __repr__(self):
        return '{ room: ' + self.name + ' n_to: ' + self.n_to.name + ' s_to: ' + self.s_to.name + ' e_to: ' + self.e_to.name + ' w_to: ' + self.w_to.name + ' }'
    
    def possible_directions(self):
        directions = {}
        directions.update({ 'n': self.n_to, 's': self.s_to, 'w': self.w_to, 'e': self.e_to})
        msg = f'You choices are: '
        for d, r in dict(directions).items():
            if  r is None:
                del directions[d]
            if r != None:
                msg += d + " "
        print(msg)
        return list(directions.values())
        
    def list_items(self):
        print(f'There is: {self.items}') 
        return [item.name for item in self.items] 

    def hasitem(self, item_name):
        return item_name in self.list_items()
    
    def new_room(self, direction):
        print(direction)
        new = self.__getattribute__(direction)

        return new