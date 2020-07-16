# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, room, description):
        self.room = room
        self.description = description
        self.n_to = None
        self.e_to = None
        self.s_to = None
        self.w_to = None

    def __str__(self):
        return f'Location: {self.room}. {self.description}..\n'

    def movement_choice(self, decision):
        if decision == 'n':
            return self.n_to
        if decision == 'e':
            return self.e_to
        if decision == 's':
            return self.s_to
        if decision == 'w':
            return self.w_to
        else:
            return None 