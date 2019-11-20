class NameStorage:
    def __init__(self, name: str, storage: list=[]):
        self.name = name
        self.storage = storage

class Description(NameStorage):
    def __init__(self, name: str, description: str, storage: list=[]):
        super().__init__(name, storage=storage)
        self.description = description
    # string representation of our class in the console
    # without it: <room.Room object at 0x10c08f4a8>

    def __str__(self):
        return f'Name: {self.name}\nDescription: {self.description}'
    
    def __repr__(self):
        return f'Name: {self.name}\nDescription: {self.description}'
