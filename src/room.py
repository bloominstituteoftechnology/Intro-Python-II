class Room:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.items = []

    def __repr__(self):
        print(f"-" * 40)
        return (f"You are at the {self.title}.")

    def add_item(self, item):
        return self.items.append(item)
