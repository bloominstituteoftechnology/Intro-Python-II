class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description
    def on_take(self):
        print(f"You have picked up a(n) {self.name}")
    def on_drop(self):
        print(f"You have dropped a(n) {self.name}")