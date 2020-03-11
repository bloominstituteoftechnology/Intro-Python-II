# Write a class to hold player information, e.g. what room they are in
# currently.

class Player():
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
    def move(self):
        direction = input('Do you go (n)orth, (s)outh, (e)ast, or (w)est? \n')
        if direction == 'n' and self.current_room.n_to != None:
                self.current_room = self.current_room.n_to
        elif direction == 's' and self.current_room.s_to != None:
                self.current_room = self.current_room.s_to
        elif direction == 'e' and self.current_room.e_to != None:  
                self.current_room = self.current_room.e_to
        elif direction == 'w' and self.current_room.w_to != None:
                self.current_room = self.current_room.w_to
        else:
            print('Invalid input, try again.\n')
            self.move()
            
