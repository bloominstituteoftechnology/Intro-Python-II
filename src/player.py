# Write a class to hold player information, e.g. what room they are in
# currently.
#initial commit for branch
class Player():
    def __init__(self, name,room ):
        self.name=name
        self.current_room = room
    def move (self,direction):
        if direction =='n':
            self.current_room= self.current_room.n_to
        if direction =='s':
            self.current_room= self.current_room.s_to
        if direction =='e':
            self.current_room= self.current_room.e_to
        if direction =='w':
            self.current_room= self.current_room.w_to
    def __str__ (self):
        return (f"Player {self.name} is currently in {self.current_room.name}")

