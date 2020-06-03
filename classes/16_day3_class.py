my_list = []

class Student:
    
    def __init__(me, first_name, last_name):
        me.first_name = first_name
        me.last_name = last_name
        my_list.append(me)
    
    def __str__(self):
        reutrn f"This student's name is {me.last_name}, {me.first_name}".

self = Student("Matt", "McCarley")

#python tutor
print(self.my_list)
you = Student("Sean", "Yo")

class Point():
    def __init__(self, x, y):
        self.x = x 
        self.y = y
    def __repr__(self):
        return f"Point(x={self.x}, y={self.y})"   

my_point = Point(Point(3,5))          
