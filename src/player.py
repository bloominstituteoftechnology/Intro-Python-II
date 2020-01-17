# Write a class to hold player information, e.g. what room they are in
# currently.

from room import Thee_Room
class Player:
    def __init__(self, name, starting_room):

        self.name = name
        self.current_room = starting_room
        self.items = []

    def move_player(self, inp):
        if inp == "q":
            print('Thanks for playing!')
            return True
        

        else:
            possible_room = getattr(self.current_room, (f"{inp}_to"))
            

        if possible_room == None:
            print("There is nothing in that direction")
            self.input_instructions()
            

        else:
            self.current_room = possible_room
            

                        
        

            

    def input_instructions(self):

        self.current_room.where_am_i()
        user_input = input(
                           "What would you like to do?\nTo move type: n,s,e,w\n"
                           +"to pick up an item type 'get <item>'\n"
                           +"to drop an item type 'drop <item>'\n"
                           +"Type 'i' to view inventory\n"
                           +"Type 'q' to quit\n")
        return self.check_input(user_input)

    def check_input(self, inp):
        text = inp.split(" ")
        move_list = ['n', 'e', 's', 'w', 'q']
        action_list = ['get', 'drop', 'take']
        inv = ['i', 'inventory','list', 'inv']
        if inp in move_list:
            return self.move_player(inp)
        elif inp in inv:
            self.list_inventory()
        elif text[0] in action_list and len(text) > 1:
            if text[0] == 'get' or text[0] == 'take':
                self.get_item(text[1])
            else:
                self.drop_item(text[1])

        else:
            print("Incorrect Input. Please Try Again!")

    def list_inventory(self):
        print("checking inventory...")
        if len(self.items) > 0:
            for x in self.items:
                print(x.name)
        else:
            print("You are holding nothing")


    def get_item(self, item):
        for obj in self.current_room.items:
            if obj.name == item:
                obj.on_take()
                self.current_room.items.remove(obj)
                self.items.append(obj)
                return
        print("That item is not in this room")


    def drop_item(self,item):
        for obj in self.items:
            if obj.name == item:
                obj.on_drop()
                self.current_room.items.append(obj)
                self.items.remove(obj)
                return
        print("You are not holding that item")







