############ class methad and self ####
### add method to the car class that disylays the full name of the car #

class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
        
    def full_name(self):
        return f"{self.brand}{self.model}"
    
my_car=Car("Toyota","Corolla")
print(my_car.brand)                            
print(my_car.model)  
print(my_car.full_name())
            