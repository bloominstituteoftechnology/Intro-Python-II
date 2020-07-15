# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room

    def move(self, string):
        control_mapping = {
            "n":self.current_room.n_to,
            "e":self.current_room.e_to,
            "s":self.current_room.s_to,
            "w":self.current_room.w_to,
        }
        try:
            if control_mapping[string] == None:
                print('\nInvalid direction.')
            else:
                self.current_room = control_mapping[string]
        except:
            print('\nInvalid command.')