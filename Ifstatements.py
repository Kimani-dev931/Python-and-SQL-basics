# if statements
x=2
marks=49
grade=2000
if(x>0):
    print("The number is positive")
#if...else statement
if(marks>=50):
    print("You have passed the exam")
else:
    print("You have failed your exam")
# if...elif..else statement
if(grade>=0 and grade<=29):
    print("You failed")
elif grade>=30 and grade<=49:
    print("You have passed")
elif grade>=50 and grade<=79:
    print("You have a credit")
elif grade>=80 and grade<=100:
    print("You have a distinction")
else:
    print("Wrong grade entered")
# Assignment
username="kims931"
password="kims"
value1=input("Enter your username")
value2=input("Enter your password ")
if username==value1 and password==value2:
    print("your login was successful")
elif username!=value1 and password==value2:
    print("your username or password is wrong try again")


