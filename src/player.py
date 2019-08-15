from item import Inventory

class Player(Inventory):
  def __init__(self, name, current_room, items = None):
    self.name = name
    self.current_room = current_room
    self.items = items

    super().__init__()

  def __str__(self):
    return f"{self.name}, {self.current_room}"

  def action_input(self, decision):
    if decision == 'n':
      if self.current_room.n_to is not None:
          self.current_room = self.current_room.n_to
    elif decision == 's':
      if self.current_room.s_to is not None:
        self.current_room = self.current_room.s_to
    elif decision == 'e':
      if self.current_room.e_to is not None:
        self.current_room = self.current_room.e_to
    elif decision == 'w':
      if self.current_room.w_to is not None:
        self.current_room = self.current_room.w_to
    else:
      print("Thanks for playing")

  def display_room(self):
    print(f'Current Room: {self.current_room.name}\n \n{self.current_room.description}\n\n')

