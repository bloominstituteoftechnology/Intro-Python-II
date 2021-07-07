
class Room:
    '''
    This is a room class
    '''
    def __init__(self, title, description, items):
        self.title = title
        self.description = description
        self.items = items
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None        
    def __str__(self):
        '''
        This is a string method
        '''
        return f"{self.title}\n\n{self.description}"





        # # Implement a class to hold room information. This should have name and
# # description attributes.

# class Room: 
#     def __init__(self, title, description, n_to=None, s_to=None, e_to=None, w_to=None):
#         self.room = room
#         self.title = title
#         self.description = description 
#         self.n_to = n_to 
#         self.s_to = s_to 
#         self.e_to = e_to 
#         self.w_to = w_to
#     def __str__(self): 
#         return f"{self.title}\n\n{self.description}"