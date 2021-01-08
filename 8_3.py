class memory:
    def __init__(self,internal,secondary,ram):
        self.internal=internal
        self.secondary=secondary
        self.ram=ram

    def getinfo(self):
        print("internal:{} , secondary:{} and ram:{}".format(self.internal,self.secondary,self.ram))

class mobile(memory):
    def __init__(self,model,brand,price,memory):
        self.model=model
        self.brand=brand
        self.price=price
        self.memory=memory

    def mobile1(self):
        print("Mobile model:",self.model)
        print("mobile brand:",self.brand)
        print("mobile price:",self.price)
        print("mobile memory:",end=" ")
        self.memory.getinfo()

m=memory("32gb","64gb","4gb")
m1=mobile("nokia","620","10000",m)
m1.mobile1()        
