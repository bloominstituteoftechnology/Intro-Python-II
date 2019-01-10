# Implement a class to hold room information. This should have name
# and description attributes.

# Encapsulation - Every object needs some sort of external-facing
# API in order to manipulate its internal state.

# Inheritance - Allows us to leverage pre-existing code that exists
# on a base class.
# Explicitly forms an object hierarchy.

# Polymorphism - Hot swapping various pieces. Similar to modularity.

# In Python, you should use dictionaries to store key-value pairs

class Location:
  def __init__(self, name, description, items = []):
    self.name = name
    self.description = description
    self.items = items