class Item:
    # constructor
    def __init__(self, name, description):
        self.name = name
        self.description = description
    # default representation
    def __repr__(self):
        return(f'{self.name} has description: {self.description}')
    