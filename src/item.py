class Item():
    def __init__(self, name, description):
        self.name = name
        self.description = description
        return

    def __str__(self):
        return (self.name)

    def on_take(self):
        print('You have picked up ', self.description)
        return

    def on_drop(self):
        print('You have dropped ', self.description)
        return