# Implement a class to hold room information. This should have name and
# description attributes.

# from READme
# Put the Room class in room.py based on what you see in adv.py.
# : in adv.py I see a room object with keys of room names, and invoking
# the Room class and within the parenthesis, a 2 quotes (a detailed room name)
# and a short message.

class Room:
    def __init__(self, r_name, r_description, items=[]): # Room was extended with a list
        self.r_name = r_name
        self.r_description = r_description
        self.items = items

        self.n_to=None
        self.s_to=None
        self.e_to=None
        self.w_to=None
    


print("inside class Room",)