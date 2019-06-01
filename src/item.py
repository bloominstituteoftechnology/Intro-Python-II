class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        # self.items = items
        
    def __str__(self):
        return self.name
    
    def on_grab(self, player):
        print("...got it")

        player.items.append(self)

        player.room.items.remove(self)

class Treasure(Item):
    def __init__(self, name, description, value):
        super().__init__(name, description)
        self.value = value
        self.picked_up = False

    def on_grab(self, player):
        super().on_grab(player)
        if not self.picked_up: 
            player.score += self.value
            self.picked_up = True
