# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, area, description, contains=[]):
        self.area = area
        self.description = description
        self.contains = contains
    
    def add_item(self, item):
        self.contains.append(item)
    
    def remove_item(self, item):
        for i, j in enumerate(self.contains):
            if j == item:
                del self.contains[i]
            # print(i, j, item)

    def __repr__(self):
        return f'Area: {self.area}, Description: {self.description}, Items: {self.contains}'