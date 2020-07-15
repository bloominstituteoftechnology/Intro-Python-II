# Implement a class to hold room information. This should have name and
# description attributes.
import random

class Room:
    def __init__(self, name, desc, items=None):
        self.name = name
        self.desc = desc
        self.items = items
    def __getitem__(self, name):
        return getattr(self, name)
    def get_item(self):
        if self.items:
            selected_item = input(f"Room's items:\n\
{', '.join(self.items)}, random\n")
            if selected_item == 'random':
                item = random.choice(self.items)
                self.items.remove(item)
                return item
            else:
                try:
                    item_index = self.items.index(selected_item)
                    return self.items.pop(item_index)
                except:
                    print("Item not found, try again.")
                    self.get_item()
        return False