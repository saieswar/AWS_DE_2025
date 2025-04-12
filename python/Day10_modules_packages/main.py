

import Cal as c   
a = 5 
b = 6

c1 = c.add(a, b)
print(c1) 





from Cal import mul, sub
a = 5
b = 6
c2 = sub(a, b)
print("sub",c2)
print(mul(a,b))


from plyer import notification

import time   
from plyer import notification

while True:
    print("Please sip some water!")  
    notification.notify(title="Please drink some water", 
                        message = "You need to drink some water",)
    time.sleep(10)