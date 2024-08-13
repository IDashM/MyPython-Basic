import sys
import math
import random
import threading
import time

age = random.randint(1,40)

if age < 5:
    print("Stay Home")
elif (age >= 5) and (age <= 6):
    print("Go to Kinder School")
elif (age > 6) and (age <= 17):
    print("Go to High School")
else:
    print("You are College")


print(age)