# Implement a class to hold room information. This should have name and
# description attributes.
import textwrap
class Room:
  def __init__(self, name, description):
    self.name = name
    self.description = description

  def __str__(self):
    wrap = textwrap.TextWrapper(width = 40)

    wrap.wrap(text = self.name + "\n\n" + self.description + "\n\n")