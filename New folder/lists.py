import sys
import math
import random
import threading
import time

#      0   1    2       3
l1 = {1, 3.14, "DEREK",True}
print("Lenght", len(l1)) # gets the number of arrays 
print("1st ", list(l1)[0])
print("Last ", list(l1)[-1])
list(l1)[0] = 2
list(l1)[2:4] = ["Bob",False]
list(l1)[2:2] = ["Paul", 9]


print(l1)
