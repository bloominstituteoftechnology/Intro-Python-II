# Write a class to hold player information, e.g. what room they are in
# currently.
class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self): 
        return f'{self.name}, {self.description}'