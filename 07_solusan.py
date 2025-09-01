#########  STATIC METHOD ##########


class Car:
    
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model


    @staticmethod
    def general_description():
         return "Car are means of transport"
     


Car("Tata","Nrxon")
print(Car.general_description())           # Car are means of transport