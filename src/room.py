# Implement a class to hold room information. This should have name and
# description attributes.
# Implement a class to hold room information. This should have name and
# description attributes.

class Room (object):
    def __init__(self,name,description,items = [], is_light = None):
        """
        Will initialize name description items is_light for the Room class.
        """
        self.name = name
        self.description = description
        self.items = items
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.directions = []
        self.is_light = is_light
    def __str__(self):
        """
        will return the Room properties back as a string. 
        """
        return f"Room name: {self.name}\n\n, Room description: {self.description}\n\n Room has light : {self.is_light}"
    def revealItems(self):
        items = []
        for item in self.items:
            items.append((item.name, f"description {item.description}"))
        return (f"This room includes the following: {items}\n\n to pick up these items use keyword grab item_name\n\n")
    def getDirections(self):
        """
        This function will return the directions and the rooms in those directions. 
        """
        return f"n: {self.n_to}, \n\n s: {self.s_to}, \n\n e: {self.e_to},\n\n w: {self.w_to}\n\n"
    def change_room(self, option):
        """
        will return the room asscoaited with the choice between e  w   s  n
        if the user makes in valid choice or even a false enter where nothing is entered in or 
        a choice longer than required None is returned after a message printed letting the user 
        know what they did wrong.
        """
        option = option.lower()
        if len(option) != 1:
            print("Please choose from the following\n\n e\n w\n s\n n\n")
            return None
        if option == "n" and self.n_to is not None: 
            print("n : You chose to go North")
            return self.s_to
        elif option == "s" and self.s_to is not None:
            print("s : You chose to go South")
            return self.s_to
        elif option == "w" and self.w_to is not None:
            print("w : You chose to go West")
            return self.w_to
        elif option == "e" and self.e_to is not None:
            print("e: You chose to go East")
        else:
            print("No room in that direction.")
            return None
    def removeItem(self, item):
        """
        This function will take care of removing the itme if self.items has the item. 
        returns a string of the item removed else returns None. 
        """
        if self.items.count(item) >  0: 
            self.items.remove(item)
            return(f"{item.name} has been removed from the {self.name}\n\n to drop an item use drop item_name\n\n to check your inventory use i\n\n")
        else: 
            return None
        def addItem(self, item):
            """
            adding item to the room
            """
            self.items.append(item)


