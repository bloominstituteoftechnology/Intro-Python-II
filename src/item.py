class Item():
   
    def __init__(self, name, description):
        self.name = name
        self.description = description
       
 
    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\n".format(self.name, self.description)