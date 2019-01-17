class Items:
    def __init__(self, name, description):
        self.name = name
        self.description = description
    def __repr__(self):
        print(f"{self.name}, {self.description}")