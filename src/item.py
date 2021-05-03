class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __repr__(self):
        str_rep = f"""Item({self.name}, {self.description})"""
        return str_rep

    def __str__(self):
        str_rep = f"{self.name}, {self.description}"
        return str_rep