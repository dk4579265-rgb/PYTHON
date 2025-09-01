##########  BASIC  CLASS OBJECT ###########
class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
        
    
my_car=Car("Toyota","Corolla")
print(my_car.brand)                            #Toyota
print(my_car.model)                            #corolla


my_new_car=Car("Tata","safari")
print(my_new_car.model)                         #Tata
print(my_new_car.brand)                           #safari