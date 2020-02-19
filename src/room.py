# Implement a class to hold room information. This should have name and
# description attributes.


class Room():
    def __init__(self, name, description, items=None):
        self.name = name
        self.description = description
        self.items = items

    def __str__(self):
        if(self.items == None):
            return f'This is the {self.name}. {self.description}'
        else:
            return f'This is the {self.name}. {self.description} and has {self.items}'

    def room_items(self):
