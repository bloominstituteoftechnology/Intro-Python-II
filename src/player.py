# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.inventory = []
    def get_items_selector(self):
        return ", ".join([str(f"{i}") for i in self.inventory])
    def travel(self, direction):
        if direction in ["n", "e", "s", "w"]:
            next_room = self.current_room.get_room_in_direction(direction)
            if next_room is not None:
                self.current_room = next_room
                print(f'Current Room:\n{self.current_room}\n')
            else:
                print("You cannot move in this direction.\n")
                print(f'Current Room:\n{self.current_room}\n')
    def handle_action(self, action, value):
        # print("worked")
        if action == "grab":
            object_in_room = self.current_room.find_item_by_string(value)
            # print(f'object in hand of player: {object_in_room}') 
            self.inventory.append(object_in_room)
            print(f'Player inventory after grab: {self.inventory}\n')
        elif action == "drop":
            for index2, val_loop in enumerate(self.inventory):
                # print(val_loop)
                if val_loop.name == value:
                    # print(f"{value} is valid, index: {index2}")
                    add_val = self.inventory[index2]
                    self.current_room.add_item(add_val)
                    del self.inventory[index2]
                    print(f"Player inventory after drop: {self.inventory}\n")

    
    # def return_current_room(self):
    #     return self.current_room
    # def player_inventory_reveal(self):
    #     return self.inventory

