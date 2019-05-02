class NameStorage:
    def __init__(self, name, storage = []):
        self.name = name
        self.storage = storage

class Description(NameStorage):
    def __init__(self, name, description, storage = []):
        super().__init__(name, storage = storage)
        self.description = description

    def __str__(self):
        return f'Name: {self.name}\nDescription: {self.description}'

    def __repr__(self):
        return f'Name: {self.name}\nDescription: {self.description}\n'