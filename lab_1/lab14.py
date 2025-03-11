class circle:
    def __init__(self,radius):
        self.radius=radius
        pass
    def perimeter(self):
        return 2*3.14*self.radius
    def area(self):
        return 3.14*self.radius**2
radius=float(input("enter the radius of the circle"))
object=circle(radius)
print(f"perimeter is {object.perimeter()}")
print(f"area is {object.area()}")


