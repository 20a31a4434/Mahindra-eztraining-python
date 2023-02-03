"""
#program:1
import random as r
x="i love sweets"
print(r.sample(x,2))
#everytime it gives a different output
a=[1,2,3,4,5,6]
r.shuffle(a)
print(a)
#everytime it gives a different output
a=[1,2,3,4,5,6]
print(r.choice(a))
#everytime it gives a different output
b="welcome back"
print(r.choice(b))

#
a=r.random()
print(a)
#will return random nnumbers between 0.0 and 1.0
#0.0 includes(it takes the value) and 1.0 excludes(it doen't take the value)
print(r.randint(20,30))

#
a=[10,20,30,40,50]
print(r.choices(a,k=3))  #except k none other values work
print(r.uniform(5,10))

#returns amy random number between the range includes the range values
z=dir(r)
print(z)
"""

"""
#program 2:-DISPLAY WHOLE YEAR CALENDAR

import calendar

print("FULL CALENDAR")
print(calendar.calendar(2022))

print("PARTICULAR MONTH")
print(calendar.month(2022,4))

print("SET FIRST DAY OF THE WEEK")  #used to print the week day of day 1 in month  
calendar.setfirstweekday(calendar.FRIDAY)
print(calendar.month(2022,4))
"""


"""
#program 3:- display date time

import datetime
a=datetime.datetime.now()
print(a)

sv=a.strftime("%y")  #lower case used to get the short form of the year i.e.23 from 2023
fv=a.strftime("%Y") #upper case used to get the complete year i.e 2023
print("Year short version",sv)
print("Year full version",fv)
"""
"""
#program-4:- without arguments,without return value
def multi():
    n1=int(input("NUMBER="))
    n2=int(input("NUMBER="))
    n3=int(input("NUMBER="))
    prod=n1*n2*n3
    print(prod)
multi()
"""
"""
#program-5:-without arguments and with return value

def multi():
    n1=int(input("NUMBER="))
    n2=int(input("NUMBER="))
    n3=int(input("NUMBER="))
    prod=n1*n2*n3
    return prod
res=multi()
print(res)
"""

"""
#program-6:-with arguments and without return values

def multi(n1,n2,n3):
    prod=n1*n2*n3
    print(prod)

multi(1,2,2) #numbers need to be taken because without them the result will be error

        #OR
def multi1(a,b,c):
    prod=a*b*c
    print (prod)

n1=int(input("Enter 1: "))

n2=int(input("Enter 2: "))

n3=int (input("Enter 3:"))

multi1(n1, n2, n3)
"""

"""
#program-7:- with return value and with arguments

#static input

def multi(n1, n2, n3):
    prod=n1*n2*n3
    return prod

res=multi (3,4,5)
print(res)

#User input

def multi1(a,b,c):
    prod=a*b*c
    return prod

n1=int (input("Enter 1: "))
n2=int (input("Enter 2: "))
n3=int (input("Enter 3: "))
res1=multi1(n1, n2, n3)

print (res1)
"""

'''
#program-8:- lemons program(more or less) using functions type-1
def lemon_offering():
    n=int(input("NUMBER OF LEMONS AT HAND="))
    if(n>21):
        print("THE NUMBER OF LEMONS REQUIRED ARE EXCEEDING")
    elif(n<21):
        print("THE NUMBER OF LEMONS REQUIRED ARE INSUFFICIENT")
    else:
        print("WE HAVE THE  REQUIRED NUMBER OF LEMONS")

lemon_offering()
'''
'''
#program-9:-find the factors of a number using functions type-2

def factors(x):
   print("The factors of",x,"are:")
   for i in range(1, x + 1):
       if x % i == 0:
           print(i)

num =int(input("ENTER A NUMBER TO GET THE FACTORS: "))

factors(num)
'''
"""
#program-10:-print multiplication table of a number using function type-3

def multiplication_tables(x):
    for i in range(1,11):
        print(i,"X",x,"=",i*x)

x=int(input("THE NUMBER TO WHICH THE TABLE IS CREATED="))

multiplication_tables(x)
"""

"""
#program-11:-find out sum of digits of the given number using functions type-4

def sum_of_digits(n):
    sum = 0
    for digit in str(n): 
      sum += int(digit)      
    return sum
   
n=int(input("THE NUMBER TO WHICH WE NEED TO FIN THE SUM OF DIGITS="))
print(sum_of_digits(n))

  #(OR)

def digits(n):
    sum=0
    while n!=0:
        rem=n%10
        sum=sum+rem
        n=n//10
    return sum

n=int(input("ENTER THE NUMBER: "))
res=digits(n)
print(res)
"""
"""
#program-12:- recusrsive function
def fact(n):
    if n==0:
        return 1
    return n* fact(n-1) #function calls-its call
a=int(input("enter a value: "))
result=fact(a)
print(result)
"""
"""
#program-13:-fibbonachi series without recursive functions

n=int(input("Enter number = "))
a=0
b=1
sum=0
count=1

while (count <= n):
    print (sum, end = " ")
    count += 1
    a=b
    b = sum
    sum = a + b
"""
"""
#program-14:-neon number
def neon(n):
    sum=0
    sq=n*n
    while (sq!=0):
        s=sq%10
        sum=sum+s
        sq=sq//10
    if sum==n:
        print("neon")
    else:
        print("not a neon")
a=int(input("enter a: "))
neon (a)
"""
"""
#program-15:-
#Function returns more values:
#Addition & subtraction of 2 numbers in one function

def add_sub(x,y):
    sub=x-y
    add=x+y
    return sub,add
res1,res2=add_sub(20,10)
print (res1)
print (res2)
"""
"""
#program-16:-
#variable length method
def summ(*a):
    c=0
    for i in a:
        c=c+i
    print (c)
summ(10,2,3)
"""



