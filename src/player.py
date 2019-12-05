# Write a class to hold player information, e.g. what room they are in
# currently.
class Player():
    '''this will be for the initial player info'''
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.inventory = []
        
    def __str__(self):
        return f'{self.name} is located in the {self.current_room}.'

    
    