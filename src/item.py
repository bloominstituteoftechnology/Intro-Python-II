class Item():
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def pick_up(self):
        print(f"{self.name} was picked up.")

    def drop(self):
        print(f"{self.name} was dropped.")