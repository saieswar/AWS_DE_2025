# Think in objects , we are happy in functions right?
# real world mobile, camera, laptop , 
# person -> employee 
# every object have attributes (data/prop) & methods (behaviour)'
# so if you need to store in data - attributes
# if you have complex problem ---- from now we think in obj 

# Concept class & object
# when you say obj - mobile, fan & car -- these are all manufactured
# suppose your ph is made in chaina people say it oneplus or iphone etc.. imp is where it is
#manufactured , designed -- manufactured --which is class 


#class - design , obj is instance

#so if you have a class you can design many obj

# so first is class or obj?

#integer, string, float

class Computer:
    #attriuts
    #methods
    
    def __init__(self, cpu, ram):
        self.cpu = cpu 
        self.ram = ram  #no need have same name  
        print("init called")

    def config(self):
        print("i7, 16gb, 1TB")
    
    def config1(self):
        print("config is",self.cpu, self.ram)

a = 5 
print(type(5)) # int
#com1 = Computer()
#print(type(com1))
#every thing is obj in python

#question how to call config func?
#Computer.config()  # error for which obj

# Computer.config(com1) 

# com2 = Computer()

# Computer.config(com2)

# print("below are obj calling")
# com1.config()

#a.bit_length()



## init method
# now i want two variables  1) CPU and 2) RAM 
#__init__ 

com4 = Computer('i5', 16)
com4.config1()
#every obj have its own val



class Computer1:
    pass

c1 = Computer1()
print(id(c1))

c2 = Computer1()
print(id(c2))
# who will decide size  - depends on size of var, -- constructor defines the size 


class Computer2:
    def __init__(self):
        self.name = "sai"
        self.age = 23 


    def update(self):
        self.age = 30 


    def compare(self,other):
        if self.age == other.age:
            return True 
        else:
            return False


c1 = Computer2()
c2 = Computer2()
print(c1.name)
c1.age = "30"
print(c1.age)

if c1.compare(c2) :
    print("same comparison age")







class Car:
    wheels = 4
    def __init__(self):
        self.mileage = 10
        self.company = "BMW"
    

c1 = Car()
c2 = Car()
print(c1.mileage, c1.mileage)
print(c2.mileage, c2.mileage)

c1.mileage=8 

# so it will change only c1 


# now i want to change a var to all over the class 
#def var inside init = instance var & out side inint it is class 


# class name space and instance name space 
#so, use Car.wheels = 5 





class Student:

    school = 'oxford'
    def __init__(self,m1,m2,m3):
        self.m1 = m1 
        self.m2 = m2 
        self.m3 = m3 

    def average(self): # self passing it is instance method
        return (self.m1 + self.m2 + self.m3)/3 
    
    @classmethod
    def info(cls):
        return cls.school
    

s1 = Student(23,4,5)
s2 = Student(99,23,55)

print("ave",s1.average())


# fetc m1 get_M1(self) - acccesor , update - def set_m1(self,val) --> instance methods


# if u want to work with class var use class method 
# Student.info() - err 