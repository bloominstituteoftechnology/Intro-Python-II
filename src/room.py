# Implement a class to hold room information. This should have name and
# description attributes.

from fixed import Fixed


class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.n_to = None
        self.e_to = None
        self.s_to = None
        self.w_to = None
        self.n_blocked_by = None
        self.e_blocked_by = None
        self.s_blocked_by = None
        self.w_blocked_by = None
        self.items = {}

    def __str__(self):
        if self.name.startswith('Outside'):
            val = f'You are {self.name}.'
        else:
            val = f'You are in the {self.name}.'
        val += f'\n{self.description}\n'

        if self.n_blocked_by != None and self.n_blocked_by.removed == False:
            val += f'{self.n_blocked_by.a_or_an()} {self.n_blocked_by.name} blocks the way North. '
        if self.e_blocked_by != None and self.e_blocked_by.removed == False:
            val += f'{self.e_blocked_by.a_or_an()} {self.e_blocked_by.name} blocks the way East. '
        if self.s_blocked_by != None and self.s_blocked_by.removed == False:
            val += f'{self.s_blocked_by.a_or_an()} {self.s_blocked_by.name} blocks the way South. '
        if self.w_blocked_by != None and self.w_blocked_by.removed == False:
            val += f'{self.w_blocked_by.a_or_an()} {self.w_blocked_by.name} blocks the way West. '
        return val

    def add_item(self, item):
        self.items[item.name.lower()] = item

    def remove_item(self, item_name):
        if item_name.lower() in self.items:
            del self.items[item_name.lower()]
