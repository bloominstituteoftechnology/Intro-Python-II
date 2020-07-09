class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def on_take(self):

        print(f"You have picked up {self.name}")

# item - Room : This is aggregate relationship
#   |
# -Player
