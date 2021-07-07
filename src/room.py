# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
  def __init__(self,name,description,inventory=[]):
    self.name = name
    self.description = description
    self.inventory = inventory 

  def __repr__(self)  :
    output = "You have entered.." + str(self.name)
    output += "\n" + str(self.description)
    output += "\nIt has the following Items:"
    for item in self.inventory:
      output += "\n" + str(item)

    return output      