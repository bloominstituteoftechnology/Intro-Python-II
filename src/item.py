#  This will be the base class for specialized item types to be declared later.

class Item:
    def __init__(self, iname, idescription):
        self.iname = iname
        self.idescription = idescription

print("inside class Item",)