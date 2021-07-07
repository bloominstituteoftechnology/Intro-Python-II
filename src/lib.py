class NameStorage:
    def __init__(self, name, storage = []):
        self.name = name
        self.storage = storage

class Description(NameStorage):
    def __init__(self, name, description, storage = []):
        super().__init__(name, storage = storage)
        self.description = description