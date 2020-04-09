# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, items=None):
        self.name = name
        self.description = description
        if(items is None):
            self.items = {}
        else:
            self.items = {item.id:item for item in items}

        #Available rooms to direction
        self.n_to = None
        self.e_to = None
        self.s_to = None
        self.w_to = None
    
    # Accessor method that returns the key,value pairs of the items dict
    def view_items(self):
        return items.items()

    # Function to create a printable string of all current items in the room 
    def check_items(self):
        if(self.items is None):
            return 'No items in this room'
        else:
            base = ''
            for item in self.items:
                base = base + self.items[item].name + ', '
            return base[:-2]
    
    def add_items(self, item_list):
        # Check to make sure type of object passed is a list
        if(type(item_list) != list):
            raise TypeError('Expected a list in this method')

        # Add each item in the passed list to the items dict
        for item in item_list:
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
            return []
        
        
        
