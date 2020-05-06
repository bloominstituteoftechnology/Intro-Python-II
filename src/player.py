from item import Food, Egg

# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.item = []
    def travel(self, direction):
        if getattr(self.current_room, f"{direction}_to") is not None:
            self.current_room = getattr(self.current_room, f"{direction}_to")
            print(self.current_room.name)
            print("")
            print(self.current_room.description)
        else:
            print("You cannot move in that direction")
    def print_inventory(self):
        print("You are holding: ")
        for item in self.items:
            print(item.name)
    def eat(self, foot_item):
        if not isinstance(food_item, Food):
            print(f"You can not eat {food_item.name}")
        else:
            print(f"You have eaten {foot_item.name}, your strength is now{self.strength}")
            self.strength += food_item.calories
            self.items.remove(food_item)
