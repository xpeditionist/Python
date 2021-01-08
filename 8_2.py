class tv:
    def __init__(self,model,brand):
        self.model=model
        self.brand=brand

    def feature(self):
        print("feature")

class smarttv(tv):
    def __init__(self,model,brand,screensize,price,resolution):
        super().__init__(model,brand)
        self.screensize=screensize
        self.price=price
        self.resolution=resolution
    
    def newfeatures(self):
        print("newfeatures")

p1=smarttv("KY","Onida","16","10000","1024")
p1.newfeatures()            


