#EXCEPTION HANDING:-

#program-1
"""
a=int(input("ENTER a= "))     #we can directly take a,b values e.g:- a=75,b=86
b=int(input("ENTER b= "))
try: #you are telling this may have error
    print(a/b)

#except Exception:#you  saying error if thr i hanle
#print("Can't divide any number by zero")

except Exception as e:
    print("Please note,number can't be divided by 0",e) #this will print error also
#to check your prg execution goes till end or get
print("Bye")

"""

#program-2
'''
#whenever u open a file make sure u close it
#file may be anything - prg, database....gives

a=int(input("ENTER a= "))  #we can directly take a,b values e.g:- a=75,b=86
b=int(input("ENTER b= "))
try:
    print("resource open")
    print(a/b)

except Exception as e:
    print("Dont give second number as zero",e)

finally: # will get executed if thr is error or n
    print("Resource closed")
'''

#program-3
'''
#like specialised doctors
#for those specific error only those exception #blocks will get executed
a=10
try:
    b=int(input("Enter the number"))
    print("resource open")
    print (a/b)
except ZeroDivisionError as e:
    print("Please note, number cant be divided by 0")
except ValueError as e:
    print("Invalid input",e)
except Exception as e: #if not any above errors
    print("Other error",e)
finally:
    print("Resource closed")
'''

#program-4

#raise used to interrupt normal prg flow and raise
'''
#example-1
try:
    raise NameError("Hello Friend")
except NameError:
    print("There is a Exception")
    raise
'''
'''
#exapmle-2
x=10
if(x%2!=0):
    raise Exception("x should be even number")
else:
    print("x is even number..CORRECT")
'''

#Object Oriented Programming:- 

#program-5
'''
class computer:   #class definition
    def config(self):  #config is a function
        print("Yes")

lenova=computer() #object1
lenova.config()

dell=computer() #object2
dell.config()
'''


#program-6
'''
#constructor

class Employee:
    def __init__(self,name,id):
        self.id = id
        self.name = name
    def display (self):
        print("ID: %d \nname: %s" %(self.id, self.name))
empl=Employee("John", 101)
emp2=Employee("David", 102)
empl.display()
emp2.display()
'''

#program-7
'''
#variables and var.access in class and method
class computer():
    a=10
    b=20
    print("class variable inside class",a)

    def config(self): #config is a fuction
        c=100
        print("Yes")
        print("Instance access",self.b)

lenova=computer() #obect 1
print(lenova.a)
print(lenova.a+lenova.b)
dell=computer()
print("dell",dell.a)
lenova.config()
'''
#program-8

