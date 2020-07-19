# Write a class to hold player information, e.g. what room they are in
# currently.

class Player: 
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.inventory = []


    def __str__(self):
        # return f"{self.name}: {self.current_room}"
        output = f"{self.name}: {self.current_room}" 
        for item in self.inventory:
            output += f"\n item: {item.name}"
        return output
    
    def move(self, direction):
        if self.current_room.connections[direction] is not None:
            self.current_room = self.current_room.connections[direction]
        else: 
            print("You cannot move in that direction")
    
    def addItem(self):
        if self.current_room.items is not None:
            print("you can either take the item or leave it")
            user_input = input("Would you like to pick up an item: " + self.current_room.items.name + " ")
            if user_input == "take":
                self.inventory.append(self.current_room.items)
                print("you picked up " + self.current_room.items.name)
            else:
                print("You have choosen not to take the item")
        else:
            print("There is no items in the room")

    def dropItem(self):
        if self.current_room.items is not None:
            result = self.inventory.pop()
            print(f"you have dropped and item: {result.name}")
        else :
            print("There is nothing to drop")

