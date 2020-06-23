# Implement a class to hold room information. This should have name and
# description attributes.

import textwrap
wrapper = textwrap.TextWrapper()


class Room:

    def __init__(self, name, description, items=[]): 
        self.name = name
        self.description = description	   
        self.items = items

    def __repr__(self): 
        items = ""

        if len(self.items) > 0:  # Check to see if the room holds any items
            for (index, item) in enumerate(self.items):  # Give each item an index
                # format the list of items correctly
                if (index == 0 and len(self.items) <= 1) or (index == len(self.items) - 1):
                    items += f'{item.name} '
                else:
                    items += f'{item.name}, '
        else:
            items = "none"

        # Wrap text at 70 columns using built-in textwrap (https://docs.python.org/2/library/textwrap.html)
        item_description = wrapper.wrap(self.description)
        items = wrapper.wrap(items)

        room_details = f'\n{self.name}\n##########################\n'
        for line in item_description:
            room_details += line + '\n'

        room_details += 'Room items: '
        for line in items:
            room_details += line + "\n"

        return room_details

    def get_item(self, item):
        self.items.append(item)

    def drop_item(self, item):
        self.items.remove(item)
