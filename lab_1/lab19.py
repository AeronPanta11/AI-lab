class car:
    class engine:
        def __init__(self):
            self.type=input("enter type of engine")
        def start(self):
            print("press Y to start engine")
            if input()=='Y':
                print("engine is started")
                es=1
            return es

        def stop(self):
            print("print N to stop engine")
            if input()=="N":
                print("engine is stopped")
                es=0
            return es
        
    class wheel:
        def __init__(self):
            self.type=input("enter type of wheel")
        def start(self):
            print("press Y to start wheel")
            if input()=='Y':
                print("wheel is started")
                ws=1
            return ws

        def stop(self):
            print("print N to stop wheel")
            if input()=="N":
                print("whell is stopped")
                ws=0
            return ws
    def __init__(self):
        self.wheel=car.wheel()
        self.engine=car.engine()
        
    def start_car(self):
        if self.wheel.start() & self.engine.start()==1:
            print("car is started")
             
                    
obj1=car()   
obj1.start_car()       
        