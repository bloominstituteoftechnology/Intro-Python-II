class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


    def __str__(self):
        return f"Product: {self.name}, Price: {self.price}"


class Clothing(Product):
    def __init__(self,name='shirt',price=20,size='m'):
        super().__init__(name, price)
        self.size = size


    def __str__(self):
        return f"Product: {self.name}, Price: {self.price} Size: {self.size}"