# Implement a class to hold room information. This should have name and
# description attributes.

# Put the Room class in room.py based on what you see in adv.py.
# The room should have name and description attributes.
# The room should also have n_to, s_to, e_to, and w_to attributes which point to the room in that respective direction.

# rooms to include: outside, foyer, overlook, narrow, treasure
class Room:

    def __init__(self, name, description):

        self.name = name
        self.description = description

    def outside(self, n_to='foyer'):

        self.n_to = n_to

    def foyer(self, s_to='outside', n_to='overlook', e_to='narrow'):

        self.s_to = s_to
        self.n_to = n_to
        self.e_to = e_to

    def overlook(self, s_to='foyer'):

        self.s_to = s_to

    def narrow(self, w_to='foyer', n_to='treasure'):

        self.w_to = w_to
        self.n_to = n_to

    def treasure(self, s_to='narrow'):

        self.s_to = s_to