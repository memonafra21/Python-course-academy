# Creating a class
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    # Method to display car information
    def car_info(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Year:", self.year)
        

# Creating objects of the class
car1 = Car("Toyota", "Corolla", 2020)
car2 = Car("Honda", "City", 2022)

# Calling method for each object
car1.car_info()
car2.car_info()
