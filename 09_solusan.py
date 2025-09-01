class Car:
    
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model
        
        
    @staticmethod
    def general_description():
         return "Car are means of transport"
     @property
     def model(self):
         return self._model