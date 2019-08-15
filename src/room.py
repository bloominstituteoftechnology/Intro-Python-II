# Implement a class to hold room information. This should have 
# name and description attributes.
  #  def __init__(self, name, description, n_to=None, s_to=None, e_to=None, w_to=None ):
class Room: 
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.w_to = None
        self.e_to = None

    # def __str__(self):
    #     roomstr = f'Room name: {self.name}, Room description: {self.description} \n'
    #     return roomstr

