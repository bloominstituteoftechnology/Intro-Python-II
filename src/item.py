class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f"Name of item: {self.name}\n" \
               f"Description of item: {self.description}"