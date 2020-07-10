class Product:
    def __init__(self, name, price, description, brand_name, sku, on_sale=False):
        # super().__init__()
        self.name = name
        self.price = price
        self.description = description
        self.brand_name = brand_name
        self.sku = sku
        self.on_sale = on_sale

    def __str__(self):
        return f"{self.name} {self.price} {self.description} {self.brand_name} {self.sku} {self.on_sale}"

new_product = Product('test name', 'price $7', 'description really nice product', 'brand good brand', 'sku 1234')
print(new_product)

class Clothing(Product):
    def __init__(self, name, price, description, brand_name, sku, color, size):
        super().__init__(name, price, description, brand_name, sku, on_sale=True )
        self.color = color
        self.size = size

    def __str__(self):
        return super().__str__() + "comes in " + self.color + ", " + self.size + " size"

new_clothing = Clothing('shirt', 'price $5', 'description tydye', 'brand_name sketchers', 'sku 123', 'color blue', 'size L')
print (new_clothing)