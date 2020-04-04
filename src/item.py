
class Item():
  def __init__(self, name, description):
    self.name = name
    self.description = description

  def __str__(self):
    return self.name + ":\n  " + self.description

  # Note: It's very, VERY bad design to have extra stateful calls
  # to resources outside of an instance within a method of that
  # instance. I will not make this function call other
  # code. This will only print. Having methods that modify objects
  # outside of the current instance is moronic, hard to reason about
  # error prone; do I really need to explain why that's a bad idea?
  # It's so obvious. I don't know why I'd even make this method in
  # the first place. This method has nothing to do with the item
  # it belongs to. It's a notification about the change of state
  # of the player. This should, if anything, be a method of the
  # player class. Would the designer of this expect a separate
  # method giving notifications for every kind of container
  # all stored in the Item class? That doesn't make sense.
  # Just add a method to the generic container class.
  # This part of the assignment is stupid.
  def on_take(self):
    print(f"You have picked up {self.name}.") 

  # See comment above. This is stupid for the same reasons.
  def on_drop(self):
    print(f"You have picked up, except the opposite, {self.name}.") 