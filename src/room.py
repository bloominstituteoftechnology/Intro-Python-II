# Implement a class to hold room information. This should have name and
# description attributes.
from item import Item

class Room:
    def __init__(self, name, description, n_to = None, s_to = None, e_to = None, w_to = None, items: [Item] = [], isLit: bool = False):
        self.name = name
        self.description = description
        self.n_to = n_to
        self.s_to = s_to
        self.e_to = e_to
        self.w_to = w_to
        self.items = items
        self.isLit = isLit

    def __str__ (self):
        if self.isLit:
            if len(self.items) == 0:
                f'\n{self.description}\nYour bag is empty.\nYou probably will not last long without equipment.\n \nWhat will you do?'
            else:
              item_list = []
              for item in self.items:
                item_list.append(item)
                if len(item_list) > 1:
                    item_string = ','.join(item_list)
                    return f'{self.description}\nYou see {item_string} in the area.\n \nWhat will you do?'
                else:
                    return f'{self.description}\nYou see {item_list[0]} in the area.\n \nWhat will you do?'
        else:
            return f'\nThe dark is all consuming.\nYou cannot see anything.'