import packages_demo.calculator as calc 

print(calc.add_numbers(3,6))


from packages_demo import calculator as cal1
print(cal1.subtract_numbers(10,5))

from packages_demo import json_demo as j 

print(j.get_course())


#from packages_demo import *   # find the reason
from packages_demo.calculator import * 
from packages_demo.json_demo import *

# from packages_demo import calculator, json_demo
# calculator.add_numbers(3,4)
print(add_numbers(2,3))
print(msg())

