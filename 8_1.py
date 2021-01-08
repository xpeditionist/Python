class car:
    def __init__(self,model,brand,colour):
        self.model=model
        self.brand=brand
        self.colour=colour

    def start(self):
        print("start")

    def move(self):
        print("move")

    def stop(self):
        print("stop")        

class BMW(car):
    def __init__(self,model,brand,colour):
        super().__init__(model,brand,colour)
            
    def autopilot(self):
        print("autopilot")

    def autogear(self):
        print("autogear")

p1=BMW("S5","Big","White")
p1.autogear()        