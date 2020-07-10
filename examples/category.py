class Category:
    def __init__(self, name): #, products)
        self.name = name
        
    def __str__(self):
        return "No products available in " + self.name