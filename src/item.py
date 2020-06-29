class Item:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __str__(self):
                return f"{self.name}, Value: {self.value}"

    def on_take(self):
        print(f"You have picked up a {self.name}")

    def on_drop(self):
        print(f"You have dropped a {self.name}")
    
    