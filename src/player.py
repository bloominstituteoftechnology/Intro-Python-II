# python player.py

class Player():
    def __init__(self, name, current_room, inventory = []):
        self.name = name
        self.current_room = current_room
        self.inventory = inventory

    def __repr__(self):
        return f"{self.name.upper()}, you are currently at the {self.current_room}."

    
    def on_take(self, item):
        item = str(item)
        if not item in self.inventory:
            self.inventory.append(item)
            print(f"You have picked up {item}!")
    
    def on_drop(self, item):
        item = str(item)
        self.inventory.remove(item)

    def move(self):
        # TODO
        pass

        

if __name__ == "__main__":
    player_1 = Player("Adam", "Kitchen")
    print(player_1)