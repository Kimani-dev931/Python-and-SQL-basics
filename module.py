# Am calling the hello function in another file
import statistics

import Mymodule
import math
import datetime
Mymodule.hello("Kimani")
print(math.sqrt(16))
print(math.e)
dataset=[3,5,9,7,3,7,1,3]
x=statistics.mean(dataset)
s=statistics.median(dataset)
v=statistics.mode(dataset)
print("The mean is",x)
print("The median is",s)
print("The mode is",v)
masaa=datetime.datetime.now()
print(masaa)