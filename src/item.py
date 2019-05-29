class Item(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def on_take(self):
        print(f'You have picked up "{self.name}" when you picked up this item.')

    def on_drop(self):
        print(f'You have dropped "{self.name}" when you dropped this item.')
