from player import Player

class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description
    def __repr__(self):
        return f"\nName: {self.name} | Description: {self.description}"

class Weapon(Item):
    pass

class Armor(Item):
    pass

class Herb(Item):
    def __init__(self, name, description, recover_hp, type_):
        super().__init__(name, description)
        self.recover_hp = recover_hp
        self.type_ = type_
    def __repr__(self):
        return f"\nName: {self.name} Description: {self.description} Recovery: {self.recover_hp}HP Type: {self.type_}"
    def recover(Player_In_Game):
        print([i for i in Player_In_Game.inventory])
        if any([i.type_ == "Herb" for i in Player_In_Game.inventory]):
            match = next((l for l in Player_In_Game.inventory if l.type_ == "Herb"), None)
            print(match)
            Player_In_Game.health = 10 + Player_In_Game.health
            print("Player Health: ", Player_In_Game.health)