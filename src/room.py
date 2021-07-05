# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, description, item_names=[]):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.item_names = item_names

    def room_describe(self):
        lengther = len('You are in the ' + self.name)
        item_lengther = len(', '.join(self.item_names))
        empty_len = len('There are no items in the room!')
        print(f'''{'-'*lengther}
You are in the {self.name}
{self.description}\n{'-'*lengther}''')
        if self.item_names:
            print(f'''Items in the room include: \
{', '.join(self.item_names)}''')
            print('-'*item_lengther)
        else:
            print('There are no items in the room!')
            print('-'*empty_len)
