from random import sample

class Bandersnatch:

    def __init__(self, current_room, name='Bandersnatch', description='a perfidious bandersnatch.'):
        self.name = name
        self.description=description
        self.current_room=current_room

    def move(self):
        directions = [self.current_room.n_to, self.current_room.e_to, self.current_room.s_to, self.current_room.w_to]

        choice = None
        while choice is None:
            choice = sample(directions, 1)[0]
            

        self.current_room = choice
