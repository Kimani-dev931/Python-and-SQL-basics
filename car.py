class Car:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year

    def printcar(self):
        print(f"The make of my car is  a {self.make} .Its model is {self.model} and it was manufactured in the year {self.year}")

car1 = Car("Mercedes Benz", "GLE", 2022)
car1.printcar()
car2 = Car("Toyota", "Toyota premio", 2021)
car2.printcar()
car3 = Car("Subaru", "Subaru XT", 2016)
car3.printcar()

class Suv(Car):
    def __init__(self,horsepower,speed,fuelconsumption):
        self.horsepower=horsepower
        self.speed=speed
        self.fuelconsumption=fuelconsumption

    def printcardetails(self):
        print(f"The car's horsepower is {self.horsepower} ,its speed is {self.speed} and its fuel consumption is {self.fuelconsumption}")

suv1=Suv("550 horse power","220 km/h", "3 litres per kilometer")
suv1.printcardetails()
suv2=Suv()
suv2.printcar()

