# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, curr_room):
        self.curr_room = curr_room

    def move_n(self):
        if self.curr_room.n_to == None:
            print("WALLLL")
            return
        self.curr_room = self.curr_room.n_to

    def move_s(self):
        if self.curr_room.s_to == None:
            print("WALLLL")
            return
        self.curr_room = self.curr_room.s_to

    def move_e(self):
        if self.curr_room.e_to == None:
            print("WALLLL")
            return
        self.curr_room = self.curr_room.e_to

    def move_w(self):
        if self.curr_room.w_to == None:
            print("WALLLL")
            return
        self.curr_room = self.curr_room.w_to
