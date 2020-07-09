# import item from Item
# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.items_list = list()

    def print_all_items(self):
        for key, value in self.items_list.items():
            print(f"{value.name},{value.description}")    

