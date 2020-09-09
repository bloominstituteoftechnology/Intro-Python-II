class Item:
    def __item__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f"{self.name}: {self:description}"

    def on_take(self):
        print(f"\nYou have picked up the {self.name} and added it to your inventory.\n")

    def on_drop(self):
        print(f"\nYou dropped the {self.name}.\n")