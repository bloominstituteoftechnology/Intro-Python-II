# A class to hold what items are in the rooms and held by the player

class Items:
    def __init__(self, item, description):
        self.item = item
        self.description = description

    def __str__(self):
        return f'You are holding {item}. {self.description}'
    
    def __repr__(self):
        return f'This is the {item}. {self.description}'