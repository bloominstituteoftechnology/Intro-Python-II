# Implement a class to hold room information. This should have name and
# description attributes.

# title and description

# create your constructor

# have parameters with the n,s, stuff

class Room:

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):

        return f'room: {self.name}, description: {self.description}'

    name = str
    description = str
    n_to = str
    s_to = str
    e_to = str
    w_to = str