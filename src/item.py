class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f"Name: {self.name}\nDescription: {self.description}"

if __name__ == "__main__":
    items = Item("sword", "it's sharp")

    print(items)