# Write a class to hold player information, e.g. what room they are in
# currently.

class Player: 

    def __int__(self, name, current_room):
        self.name = name
        self.current_room = current_room

    def __str__(self): 
        output = '\n{self.name}\nCurrent Location:{self.current_room}\n'.format(self=self)
        return output