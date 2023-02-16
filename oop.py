class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def say_hello(self):
        print(f"Hello,my name is {self.name} and my age is {self.age}")
#creating my object
person1=Person("Erick",30)
person1.say_hello()
person2=Person("Harrison",23)
person2.say_hello()
person3=Person("Kiprop",34)
person3.say_hello()


#create a class called cars with the following attributes/properties
#make.model.year then create a function that prints make,mode and year
#Then create three objects