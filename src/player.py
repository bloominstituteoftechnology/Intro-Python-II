# from colorama import Fore, Back, Style

class Player:

    def __init__(self, name, start_room):
        self.name = name
        self.current_room = start_room
        self.items = []

    def move_player(self, inp):
        if inp == "q":
            print('Thank You for playing my adventure game!')
            return True
        # returning True to quit game

        else:
            possible_room = getattr(self.current_room, (f"{inp}_to"))
            # Check what room exists in the direction inputted

        if possible_room == None:
            print("Sorry there is nothing in this direction, please select another direction")
            self.input_instructions()
            # No room exists, continue loop

        else:
            self.current_room = possible_room

    def input_instructions(self):

        self.current_room.where_am_i()
        user_input = input(f"*******************************************************************\nHow would you like to proceed?\nTo move to another room please type: n,e,s,w\n\n*******************************************************************\n"
                           +"If you would like to pick up an item please type: 'get <item>'\n"
                           +"If you would like to drop an item please type: 'drop <item>'\n"
                           +"To view your inventory please type: 'i'\n"
                           +"If you would like to quit the game please type: 'q'\n")
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
            print("That input was not valid. Please try again!")

    def list_inventory(self):
        print(f"**************************************************************\nInventory\n**************************************************************")
        if len(self.items) > 0:
            for x in self.items:
                print(x.name)
        else:
            print("At the moment you are not holding any items!")

# switch to on take/ on drop in item.py
    def get_item(self, item):
        for obj in self.current_room.items:
            if obj.name == item:
                obj.on_take()
                self.current_room.items.remove(obj)
                self.items.append(obj)
                return
        print("There is not that kind of item in this room")


    def drop_item(self,item):
        for obj in self.items:
            if obj.name == item:
                obj.on_drop()
                self.current_room.items.append(obj)
                self.items.remove(obj)
                return
        print("At the moment you are not holding that item")