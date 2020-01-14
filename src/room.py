# Implement a class to hold room information. This should have name and
# description attributes.
class Room:

    # n_to = Room()
    # s_to = Room()
    # e_to = Room()
    # w_to = Room()

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return 'Name: {self.name} description: {self.description}'
