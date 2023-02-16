def emobilis():
    print("This is my first function")
emobilis()
# print multiplication
def calculatesquare():
    x=5
    y=6
    print(x*y)
calculatesquare()
# print fname,lname and age
def majina(fname,lname,age):
    print(fname + lname , age)
majina("Harrison","Kimani", 20)
# print cars
def cars(model,year):
    print("I just bought a  " +model+ "   manufactured in the year" , year)
cars("Marcedesbenz S550",2022)
# print maximum
def maximum(a,b,c,d,e):
    return max(a,b,c,d,e)
result=maximum(5,15,67,0,89)
print(result)
# print minimum
def minimum(a,b,c,d,e):
    return min(a,b,c,d,e)
result=minimum(5,15,67,0,89)
print(result)
# print numbers
def print_numbers(nambari):
    for i in range(nambari):
        print(i)
print(10)