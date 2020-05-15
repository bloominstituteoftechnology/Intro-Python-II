# Write a class to hold player information, e.g. what room they are in
# currently.
from exceptions import MoveError

class Player:
    def __init__(self, name, current_room, starting_items=None):
        self.name = name
        self.current_room = current_room
        if(starting_items is None):
            self.items = {}
        else:
            self.items = starting_items

    # Accessor method to get items in player inventory
    def get_items(self):
        if(len(self.items) == 0):
            return ['Empty inventory']
        else:
            lines = []
            for item in self.items.values():
                s = 'Name: {}\n\t{}'.format(item.name, item.description)
                lines.append(s)
            return lines

    # method to move the player from one room to another based on the direction
    # Checks if the movement direction is a valid target based on the current 
    # room
    def move_player(self, target_dir):
        try:
            # Verify the chosen input direction is a valid input
            # (there is a room in that direction)
            target_room = getattr(self.current_room, '{}_to'.format(target_dir))
            if(target_room is None):
                raise MoveError(self.current_room, target_dir)

            # Move the player to that room
            self.current_room = target_room
        
        # If the movement attempted is in invalid direction, except
        except MoveError as e:
            print('You cannot move in that direction!')

    def add_items(self, item_list):
        for item in item_list:
            item.on_take()
            self.items[item.id] = item

    def remove_items(self, item_id_list):
        # Check to make sure type of object passed is a list
        if(type(item_id_list) != list):
            raise TypeError('Expected a list in this method')
        
        # Check if any of the passed item id's are in the room's item dict
        if(any([id in self.items for id in item_id_list])):
            # Create a list to represent the result of trying to remove items
            # from the items dictionary
            status = []
            removed_items = []

            # Attempt to remove all items passed to this method in the list
            for id in item_id_list:
                try:
                    # Attempt to delete key 
                    item = self.items.pop(id)

                    item.on_remove()
                    removed_items.append(item)
                    # If successful, the item will be deleted and append True to status
                    status.append(True)
                except KeyError as ke:
                    # If key is not found in items, append a False to status
                    status.append(False)

            # Return which items from list successfully were removed from items dict
            removed_item_ids = [item 
                                for item, removed 
                                in zip(item_id_list, status) 
                                if removed]
    
            return (removed_item_ids, removed_items)
        else:
            return ([],[])

    def __repr__(self):
        return self.__dict__

    def __str__(self):
        s = ''
        l = ['{}:{}'.format(key,value) for key,value in self.__dict__.items()]
        s= '\n'.join(l)
        return s
