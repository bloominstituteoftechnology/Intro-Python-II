# Implement a class to hold room information. This should have name and
# description attributes.
import textwrap
class Room:
  def __init__(self, name, description):
    self.name = name
    self.description = description

  def __str__(self):
    wrap = textwrap.TextWrapper(width = 40)
    output = f'{self.name}:\n'
    output += wrap.fill(text = '    ' + self.description)
    return output