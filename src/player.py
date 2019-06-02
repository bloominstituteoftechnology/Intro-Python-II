

class Player():
    
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room


    def __str__(self):
            return '\n{self.name}\nCurrent Location:{self.current_room}\n'.format(self=self)
