# Implement a class to hold room information. This should have name and
# description attributes.
from item import Item
class Room:
    number_of_rooms = 0
    locked = False

    def __init__(self, name, description = ''):
        self.name = name
        self.description = description
        self.linked_rooms = {}
        self.items = []
        self.character = None
        Room.number_of_rooms = Room.number_of_rooms + 1
    
    def __str__(self):
        return f'The {self.name} \n-------------------\n{self.description} \n'
       
    def __repr__(self):
        return 'Room(' + self.name + ')'
    
    def describe(self):
        print( self.description )
    
    # method for linking room together
    def link_room(self, room_to_link, direction):
        self.linked_rooms[direction] = room_to_link

    # returns a list of directions you can move in 
    def get_info(self):
        print(f'\n {self.name} \n-------------------\n{self.description} \n')
        for direction in self.linked_rooms:
            room = self.linked_rooms[direction]
            print( "The " + room.name + " is " + direction)
    
    # method for addding items to room
    def add_item_to_room(self, name, desc):
        item = Item(name, desc)
        self.items.append(item)

    # returns a list of item names that are in the room
    def list_items(self):
        names= []
        for item in self.items:
            print("*** The room contains " + item.name + "!!")
        for item in self.items:
            names.append(item.name)
        return names

    def hasitem(self, item_name):
        return item_name in self.list_items()
    
    def move(self, direction):
  
        if direction in self.linked_rooms:
            new_room = self.linked_rooms[direction]
            if new_room.locked == True:
                print('------------------- \n ****** The room is locked, you need the key!')
                return self
            return new_room
   
        else:
            print("You can't go that way")
            return self

    #  getters and setters

    # description
    def set_descrip(self, room_description):
        self.description = room_description

    def get_descrip(self):
        return self.description

    # character
    def set_character(self, character):
        self.character = character

    def get_character(self):
        return self.character

     # item
    def set_items(self, items):
        self.items = items

    def get_items(self):
        return self.items