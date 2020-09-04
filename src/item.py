class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def taken(self):
        print(f"Picked up {self.name}. May it serve you well.")

    def dropped(self):
        print(f"Dropped {self.name}. Hope you didn't need that.")

    def examine(self):
        print(f"Examining the {self.name}... \n{self.description}")
