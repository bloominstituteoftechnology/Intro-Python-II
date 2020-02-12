# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f'{self.name} {self.description}'

    # def .n_to(self):

    # def .s_to(self):

    # def .e_to(self):

    # def .w_to(self):
