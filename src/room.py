# Implement a class to hold room information. This should have name and
# description attributes.
from item import Item
import textwrap


class Room():

    def __init__(self, name, desc):
        # Initialize name and desc during creation.
        self.name = name
        self.desc = desc

        # Place holder for mapping adjacent rooms.
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None

        # Place holder for items
        self.items = []

    def __str__(self):
        output = f'{self.name}: '

        for text in textwrap.wrap(self.desc):
            output += "\n" + text

        output += f'\n\nAvailable paths [{self.available_path()}]'
        output += f'\n\n{self.available_items()}'

        return output

    def available_path(self):
        path_list = []

        if self.n_to:
            path_list.append('n')
        if self.s_to:
            path_list.append('s')
        if self.e_to:
            path_list.append('e')
        if self.w_to:
            path_list.append('w')

        return ", ".join(path_list)

    def available_items(self):
        room_item_list = self.get_items()

        output = f'{len(room_item_list)} available items in room.'

        for item in room_item_list:
            output += f'\n{item}'

        return output

    def add_item(self, item):
        self.items.append(item)

    def get_items(self):
        return self.items

    def remove_item(self, index):
        self.items.pop(index)
