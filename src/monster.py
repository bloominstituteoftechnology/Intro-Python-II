#  This is the file that will hold the monster class

class Monster:

    def __init__(self, name, weakness=None, description=None, action =None):
        self.name = name
        self.weakness=weakness
        self.description = description
        self.action = action
