class vehicle:
    def __init__(self,speed,model):
        self.speed=speed
        self.model=model

obj=vehicle(250,"Hyundai Venue N line")
obj2=vehicle(200,"Benz")
obj3=vehicle(100,"Audi")
print("Speed:",obj2.speed)
print("Model of car:",obj3.model)