class Item:

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f"ITEM: {self.name} \nINFO: {self.description}"

    def print_name(self):
        print(f"{self.name}")

    def on_take(self):
        return f"\nYou have picked up {self.name}"

    def on_drop(self):
        return f"\nYou have dropped {self.name}"

if __name__ == "__main__":
    my_item = Item("Key", "Seems to unlock something ...")
    print(my_item)