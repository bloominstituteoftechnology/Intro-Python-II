# Implement a class to hold room information. This should have name and
# description attributes.


class Room():
    def __init__(self, name, description, n_to=None, s_to=None, w_to=None, e_to=None):
        self.name = name
        self.description = description

    def __str__(self):
        return f'This is the {self.name}'
