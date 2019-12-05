# Implement a class to hold room information. This should have name and
# description attributes.

class Room():
    ''' class for room'''
    def __init__(self, description, room):
        self.room = room 
        self.description = description
   
    
    #direction attr should point to room in that direction, when added causes err
    def __str__(self):
       return f' This is {self.room}: {self.description}'
    
