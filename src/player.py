# Write a class to hold player information, e.g. what room they are in
# currently.
from utils import clear
from item import LightSource, Equipment

class Player:
    def __init__(self, location, base_hp=1, base_attack=0, base_defense=0, skills={}):
        self.location = location
        self.items = {}
        self.base_hp = base_hp
        self.base_attack = base_attack
        self.base_defense = base_defense
        self.boosted_attack = 0
        self.boosted_defense = 0
        self.skills = skills
        
    def list_items(self):
        items = ", ".join([name.__str__() for name in self.items.keys()])
        if items:
            return f"Player's items: {items}"
        return 'Player currently have no items.'

    def list_skills(self):
        skills = ", ".join([name.__str__() for name in self.skills.keys()])
        if skills:
            return f"Skills: {skills}"
        return 'Player have no skills.'
    def hasLightSource(self):
        lightSources = [item for item in self.items.values() if isinstance(item, LightSource)]
        return len(lightSources) > 0

    def move(self, direction):
        directions = ['w', 'e', 'n', 's']
        if direction not in directions:
            clear()
            print("Please enter a valid direction.")
        else:
            try:
                diff_location = self.location[f"{direction}_to"]
                self.location = diff_location
            except:
                clear()
                print("You can't move in that direction! Try again.")
                
    def loot(self, item_name):
        if self.location.dark and self.hasLightSource() == 0:
            print("Good luck finding that in the dark!")
            return
        found_item = self.location.get_item(item_name)
        if found_item:
            clear()
            found_item.on_take()
            self.items[found_item.name] = found_item
            self.update_stats()
        else:
            print('That item is not in this room.')
            
    def drop_item(self, item_name):
        if item_name in self.items:
            self.location.items[item_name] = self.items[item_name]
            self.items[item_name].on_drop()
            self.items.pop(item_name)
            return
        print(f"item {item_name} is not in inventory")
    
    def update_stats(self):
        attack = 0
        defense = 0
        for item in self.items.values():
            if isinstance(item, Equipment):
                attack += item.attack
                defense += item.defense
        self.boosted_attack = attack
        self.boosted_defense = defense
        print(f"total attack: {self.base_attack + self.boosted_attack}, total defense: {self.base_defense + self.boosted_defense}")
        

            
