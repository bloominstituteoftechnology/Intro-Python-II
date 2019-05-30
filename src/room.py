# Implement a class to hold room information. This should have name and
# description attributes.
class Room():
    def __init__(self, name, description, enemies=[], items=[]):
        self.name = name
        self.description = description 
        self.enemies = enemies 
        self.items = items 

    def __str__(self):
        return f'This is the {self.name}, {self.description}'

    