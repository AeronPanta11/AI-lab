class shape:
    def __init__(self):
        pass
    def area(self):
        return 0
    
    
class rectangle(shape):
    def area(self):
        return float(input("Length: "))*float(input("Breadth: "))
class circle(shape):
    def area(self):
        return 3.14*(float(input("radius : ")))**2

o1=rectangle()
o2=circle()
print(f"the area of rectangle is {o1.area()} and circle is {o2.area()}")
