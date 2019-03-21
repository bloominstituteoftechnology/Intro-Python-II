class Item:
    def _init_(self, name, description):
        self.name = name
        self.description = description
    def _repr_(self):
        return f"{self.name}"