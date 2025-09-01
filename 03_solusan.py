########  INHERITENSE ######
class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
        
    def full_name(self):
        return f"{self.brand}{self.model}"
    
    
class ElectricalCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size=battery_size
    

my_tesla=ElectricalCar("Tesla","Model s","85kwh")
print(my_tesla.model) 
 
 
 
 
 
 
 
"""   
my_car=Car("Toyota","Corolla")
print(my_car.brand)                            
print(my_car.model)  
print(my_car.full_name()) """   