# this is currently identical to Room, decide if its worth 

class Item:
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
    # variables are public so don't need getters 
    # def get_name(self):
    #     return self.name
 #   import ipdb; ipdb.set_trace()