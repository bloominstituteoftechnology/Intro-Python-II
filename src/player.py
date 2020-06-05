# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name,current_room):
        self.name = name
        self.current_room = current_room
      
        self.inventory = []

    
    def move_player(self, user_input):

        if hasattr(self.current_room, f"{user_input}_to"):
            self.current_room = getattr(self.current_room, f"{user_input}_to")
            print(f"You entered [{self.current_room.name}]")
            print(f"{self.current_room.description}")
        else:
        
            print("=======No Door To Next Room=======")
        
    def take_item(self, item): 
        #first check if the item present
        present = 0
        for key, value in self.current_room.items_list.items():
            if value.name.lower() == item:
                self.inventory.append(value)
                value.on_take()
                #print
                present = 1
                number = key
        if present == 1:
            self.current_room.items_list.pop(number)
        else:
            print("\n")
            print("That item isn't present in this room!")
            print("\n")

    def drop_item(self, item):
        present = 0
        for i in range(len(self.inventory)):
            
            if self.inventory[i].name.lower() == item:
                self.current_room.items_list[self.inventory[i].name] = self.inventory[i]

                self.inventory[i].on_drop()
                # print comes here
                self.inventory.pop(i)
                present = 1
            
            if present == 0:
                print("\n")
                print(f"You never had this {item} to begin with!")
                print("\n")

    def print_inventory(self):
        if len(self.inventory) > 0:
            print("↓↓↓↓::INVENTORY::↓↓↓↓") 
            for i in self.inventory:
                print(i.name)
        else:
            print("You dont have anything :/")


        
     