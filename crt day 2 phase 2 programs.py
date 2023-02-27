'''
#happy number(sum of square number which leadto 1 are happy numbres)
#4,16,37,58,89,145
def happy(n):
    s=r=0
    while(n>=0):
        for i in range(0,len(str(n))+1):
            r=n%10
            s=s+r**2
            n=n//10
        return s

n=int(input("enter the number:"))
res=n
while(res!=1 and res!=4):
    res=happy(res)
if res==1:
    print("happy number")
else:
    print("not a happy number")
'''
'''
#encap functions
#protected encap function
class encap:
    _a=10
    c=20
    def encapfunction(self):
        _b=200
        print("Encap function-accessing protected")
        print(self._a+10)
        
obj=encap()
print(obj._a)
obj.encapfunction()
print(obj.c)
#private encap
class encap:
    __a=10
    print(__a)
    def encapfunction(self):
        print("Encap function")
        print(self.__a)
obj=encap()
obj.encapfunction()
print(obj.__a)#will give error because a is private and can't be acessed outside class
#public  encap
class encap:
    a=10
    print(a)
    def encapfunction(self):
        print("Encap function")
        print(self.a)
obj=encap()
obj.encapfunction()
'''
'''
#method overloading
class moverload:
    def display(self,a=None,b=None):
        print(a,b)
obj=moverload()
print("without arguments")
obj.display()

print("with all arguments")
obj.display(20,30)

print("with one argument")
obj.display(10)
'''
'''
#method overriding
class Parent():
    #constructor
    def __init__(self):
        self.value="Inside Parent"
    #Parent's show method
    def show(self):
        print(self.value)
#defining child class
class Child(Parent):
    #constructor
    def __init__(self):
        self.value="Inside Child"
    #Child's show method
    def show(self):
        print(self.value)
obj1=Parent()
obj2=Child()
obj1.show()
obj2.show()
'''
'''
#polymorphism
class vijayawada():
    def placename(self):
        print("vijayawada placename is KLU")
    def student(self):
        print("Yes - vijayawada")
    def which_year(self):
        print("3rd year")
class hyd():
    def placename(self):
        print("hyd placename is HYD-KLU")
    def student(self):
        print("Yes - HYD")
    def which_year(self):
        print("3rd year")
obj_vij=vijayawada()
obj_hyd=hyd()
for details in (obj_vij,obj_hyd):
    details.placements()
    details.students()
    details.which_year()
'''
'''
#creating node:- declaration & definition
class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class singlelinkedlist:
    def __init__(self):
        self.head=None
    def display(self):
        if self.head is None:
            print("linked list is empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,"->", end=" ")
                temp=temp.next
obj=singlelinkedlist()
n=node(10)
obj.head=n
n1=node(21)
obj.head.next=n1
print(n1)
n2=node(30)
n1.next=n2
obj.display()
'''
'''
class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class singlelinkedlist:
    def __init__(self):
        self.head=None
    def display(self):
        if self.head is None:
            print("linked list is empty")
        else:
            temp=self.head
            while temp:
                print(temp.data, end=" ")
                temp=temp.next
obj=singlelinkedlist()
n=node("w")
obj.head=n
n1=node("i")
obj.head.next=n1

n2=node("n")
n1.next=n2
n3=node("n")
n2.next=n3
n4=node("e")
n3.next=n4
n5=node("r")
n4.next=n5
obj.display()
'''
'''
#linked list insertion at begining
class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class singlelinkedlist:
    def __init__(self):
        self.head=None
    def beginning(self,data):
        nb=node(data)
        nb.next=self.head
        self.head=nb
    def display(self):
            if self.head is None:
                print("linked list is empty")
            else:
                temp=self.head
                while temp:
                    print(temp.data)
                    temp=temp.next
obj=singlelinkedlist()
n=node("w")
obj.head=n
n1=node("i")
obj.head.next=n1

n2=node("n")
n1.next=n2
n3=node("n")
n2.next=n3
n4=node("e")
n3.next=n4
n5=node("r")
n4.next=n5

obj.beginning("sk") 
obj.display()
'''
'''
#insertion at the end
class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class singlelinkedlist:
    def __init__(self):
        self.head=None
    def beginning(self,data):
        nb=node(data)
        nb.next=self.head
        self.head=nb
    def atend(self,data):
        ne=node(data)
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=ne
    def display(self):
            if self.head is None:
                print("linked list is empty")
            else:
                temp=self.head
                while temp:
                    print(temp.data)
                    temp=temp.next
obj=singlelinkedlist()
n=node("w")
obj.head=n
n1=node("i")
obj.head.next=n1

n2=node("n")
n1.next=n2
n3=node("n")
n2.next=n3
n4=node("e")
n3.next=n4
n5=node("r")
n4.next=n5

obj.beginning("sk") 
obj.atend("uu")
obj.display()
'''
'''
#insert at a position
class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class singlelinkedlist:
    def __init__(self):
        self.head=None
   
        
    def atpos(self,pos,data):
        np=node(data)
        temp=self.head
        for i in range(pos-1):
            temp=temp.next
        np.next=temp.next
        temp.next=np
    def display(self):
            if self.head is None:
                print("linked list is empty")
            else:
                temp=self.head
                while temp:
                    print(temp.data)
                    temp=temp.next
obj=singlelinkedlist()
n=node("w")
obj.head=n
n1=node("i")
obj.head.next=n1

n2=node("n")
n1.next=n2
n3=node("n")
n2.next=n3
n4=node("e")
n3.next=n4
n5=node("r")
n4.next=n5
obj.atpos(0,"55")


obj.display()
'''
