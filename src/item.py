class Item:
    def __init__(self, name, description):
        super().__init__()
        self.name = name
        self.description = description
    
    @property
    def name(self):
        return self.name

    @name.setter
    def name(self, n):
        if " " in n:
            raise Exception('Name must be one word') 