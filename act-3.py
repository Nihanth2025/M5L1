class parrot:
    sp="bird"
    def __init__(self,name,age):
        self.name=name
        self.age=age

deer=parrot("Sambar",5)
bear=parrot("Polar bear",10)
print(deer.name)
print(deer.age)
print(bear.name)
print(bear.age)
print("Deer and bear both are ",bear.sp)
print("{} is {} year old".format(deer.name,deer.age))
print("{} is {} year old".format(bear.name,bear.age))