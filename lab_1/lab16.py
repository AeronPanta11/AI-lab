class vehicle:
    def __init__(self):
        self.make=input("please enter where it is made")
        self.model=input("please enter model number")
    def drive(self):
        print(f"Driving the {self.make} {self.model}")
        
class car(vehicle):
    def drive(self):
        print(f"Driving the {self.make} {self.model} car")

Thar=car()
Thar.drive()