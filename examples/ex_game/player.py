from item import Food, Egg

# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.items = []
        self.strength = 100
    def travel(self, direction):
        if getattr(self.current_room, f"{direction}_to"):
            self.current_room = getattr(self.current_room, f"{direction}_to")
            print(self.current_room)
        else:
            print("You cannot move in that direction")
    def print_inventory(self):
        print("You are holding: ")
        for item in self.items:
            print(item.name)
    def eat(self, food_item):
        if not isinstance(food_item, Food):
            print(f"You cannot eat {food_item.name}")
        else:
            self.strength += food_item.calories
            print(f"You have eaten {food_item.name}, your strength is now {self.strength}")
            self.items.remove(food_item)



