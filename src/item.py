class Item:
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description

    def on_take(self):
        print(f'{self.name} picked up!')

    def on_drop(self, room_name):
        print(f'Dropped {self.name} in {room_name}')
