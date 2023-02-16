try:
    print(myname)
except NameError:
    print("Myname is not defined")
except:
    print("Another issue")
