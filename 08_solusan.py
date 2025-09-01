##### PRIPERTI DECORETER  ######


class Car:
    
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model
        
        
    @staticmethod
    def general_description():
         return "Car are means of transport"
     
my_car=Car("Tata","Safari")
my_Car("Tata","Nrxon")
print(my_car.general_description())
print(Car.general_description())           