# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.item_list = []
    
    def __str__(self):
        ret = f"{self.name}\n"
        for i, c in enumerate(self.item_list):
            ret += "    " + str(i+1) + ": " + c.name +"\n"
        ret += "    " + str(1+2) + ": Exit"

        return ret

    def get_direction(self, direction):
        if direction == 'n':
            return self.n_to
        elif direction == 's':
            return self.s_to
        elif direction == 'e':
            return self.e_to
        elif direction == 'w':
            return self.w_to
        else:
            return None