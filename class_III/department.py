# should Department inherit from Store?
# In this case, may not be necessary bc there is not much functionality
# to inherit from Store
class Department:
    def __init__(self, id, name, products):
        self.id = id
        self.name = name
        self.products = products

    def __str__(self):
        return f"{self.id}: {self.name}"

    def print_products(self):
        for i, p in enumerate(self.products):
            print(f"{i+1} - {p}")