# Implement a class to hold room information. This should have name and
# description attributes.
class Room: 
    def __init__(self, name, description):
        self.name = name
        self.desc = description

    def __str__(self):
        return f"You are currently located in the {self.name}. {self.desc}."

# b = Room('bathroom', 'stinky and for pooping and stuff')
# b.n_to = 'closet'
# # b.e_to = 'kitchen'


# if hasattr(b, 'e_to'): 
#     print('room to the east exists:', b.e_to)
# else: 
#     print('room tot he east does NOT exist')