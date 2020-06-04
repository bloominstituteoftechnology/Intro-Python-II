class Drop:
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description

    def pick_up(self):
        print(f"New item: {self.name}")

    def put_down(self):
        print(f"You lost item: {self.name}")