########### polymorphism ##########

class Car:
    
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model

    def chai_brand(self):
        return self.__brand + "!"

    def full_name(self):
        return f"{self.__brand} {self.model}"

    def fuel_type(self):  # corrected method name
        return "Petrol or Diesel"

class ElectricalCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):  # overridden method
        return "Electric charge"

# Creating instances
my_tesla = ElectricalCar("Tesla", "Model S", "85kWh")
print(my_tesla.chai_brand())  # Accessing via method

safari = Car("Tata", "Safari")
safariThree=Car("Tata","Nexon")
print(safari.fuel_type())  # Calls base class method
print(my_tesla.fuel_type())  # Calls overridden method
