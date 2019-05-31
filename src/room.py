# Implement a class to hold room information. This should have name and
# description attributes.

class Room:

    def __init__(self, location, dialog, n_to=None, e_to=None, w_to=None, s_to=None):
        self.location = location
        self.dialog = dialog

    def __str__(self):
        dialogToUser = """\n{self.dialog}\n""".format(self=self)
        return dialogToUser