class Category:
    def __init__(self, name, products=None):
        self.name = name
        self.products = products
    
    def __str__(self):
        if not self.products:
            return "No products available in " + self.name
        output = self.name + ' has products: \n'
        for product in self.products:
            output += str(product)
        return output