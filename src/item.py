class Item:
    def __init__(self, name, desc, amount):
        self.name = name
        self.desc = desc
        self.amount = amount

    def __str__(self):
        return f"{self.amount} {self.desc} {self.name}"
