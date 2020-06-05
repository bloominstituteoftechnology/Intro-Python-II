class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def pick_up(self):
        print(f'You just picked up the {self.name}!')

    def drop(self):
        print(f'You just dropped the {self.name}!')
