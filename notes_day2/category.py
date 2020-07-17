from product import Product

class Category:
    def __init__(self, name, products = []):
        self.name = name
        self.products = products

    def __str__(self):
        output = ""
        if len(self.products) < 1:
            output = f"No products available in {self.name}."
        for p in self.products:
            output += "     " + str(p.price) + "\n"
        return output
        

# self.name
    # product1 on a new line 
    # product2
    # product3