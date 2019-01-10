class Item:
    '''
     base class for items
    '''
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc

    def __repr__(self):
        return (f'{self.desc}')