'''
#while creating LL we gonna do it in ascending order
#one prg multiple concepts
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def printList(self):
        temp=self.head
        if not temp:
            print('List is empty')
            return
        else:
            print('start:',end=' ')
        while temp:
            print(temp.data,end=' -> ')
            temp=temp.next
        print('end.')

    def insert(self,data):
        new_node = Node(data)

        #if the linked list is empty
        if self.head is None:
            self.head=new_node

        #if the data is smaller than the head
        elif self.head.data>=new_node.data:
            new_node.next=self.head
            self.head=new_node

        else:
            #locate the node before the insertion point
            current = self.head
            while current.next and new_node.data>current.next.data:
                current=current.next

            #insertion
            new_node.next = current.next
            current.next=new_node
            
    def delete(self, key):
        #if the list is empty
        if self.head is None:
            print("Deletion Error: The list is empty")
            return
        #if the key is in head
        if self.head.data==key:
            self.head=self.head.next
            return
        #find position of first occurrence of the node
        current = self.head
        while current:
            if current.data==key:
                break
            previous=current
            current=current.next
        #if the key was not found
        if current is None:
            print("Deletion Error:Key not found")
        else:
            previous.next=current.next
# '__'(double underscore) name is python special variable
if __name__=='__main__':
    #Create an object
    LL=LinkedList()
    print('')

    #Insert some nodes
    LL.insert(10)
    LL.insert(12)
    LL.insert(8)
    LL.insert(11)
    LL.insert(10)


    LL.printList()
    LL.delete(12)
    LL.delete(8)
    LL.delete(10)
    LL.printList()
'''

'''
#crating my modules
#functions in my another file,acting as a module fn
import fn
fn.printing()

print(__name__)


def printing():
    print("hi")
'''
'''
#lets say u have a lot of functions in ur project
#u can give all definitions at one point
#and give all functions calls inside main then thre
#easy to read ,especially for others
print("before function")
def f1():
    print("f1")
def f2():
    print("f2")
def f3():
    print("f3")
if __name__=="__main__":
    f1
    f2
    f3
print()
'''

'''
#creating linked list which goes from 1st to 2nd and 2nd to 1st nodes
class Node:
    def __init__(self,data):
        self.data=data
        self.previous=None
        self.next=None
class dll:
    def __init__(self):
        self.head=None
    def display(self):
        if self.head is None:
            print("Empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,"<-->",end=" ")
                temp=temp.next
obj=dll()
n1=Node(100)
obj.head=n1
n2=Node(200)
n2.previous=n1
n1.next=n2
obj.display()
'''
'''
#double linked list
class Node:
    def __init__(self,data):
        self.data=data
        self.previous=None
        self.next=None

class dll:
    def __init__(self):
        self.head=None
    def insert_start(self):
        n=Node(300)
        temp=self.head
        temp.previous=n
        n.next=temp
        self.head=n
                     
    def display(self):
        if self.head is None:
            print("Empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,"-->",end=" ")
                temp=temp.next
obj=dll()
n1=Node(100)
obj.head=n1
n2=Node(200)
n2.previous=n1
n1.next=n2
obj.insert_start()
obj.display()
'''
'''
#insert at pos
class Node:
    def __init__(self,data):
        self.data=data
        self.previous=None
        self.next=None
class dll:
    def __init__(self):
        self.head=None
    def insert_pos(self,pos):
        n=Node(300)
        temp=self.head
        for i in range(1,pos-1):
            temp=temp.next
            n.previous=temp
            n.next=temp.next
            temp.next.previous=n
            temp.next=n
    def display(self):
        if self.head is None:
            print("Empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,"<-->",end=" ")
                temp=temp.next
obj=dll()
n1=Node(100)
obj.head=n1
n2=Node(200)
n2.previous=n1
n1.next=n2
obj.insert_pos(2)
obj.display()
'''
'''
#deleting of first node
class Node:
    def _init_(self,data):
        self.data=data
        self.previous=None
        self.next=None
class dll:
    def _init_(self):
        self.head=None
    def delete_end(self):
        temp=self.head.next
        prev=self.head
        while temp.next is not None:
            temp=temp.next
            prev=prev.next
            prev.next=None    
   def display(self):
        if self.head is None:
            print("Empty")
        else:
            temp=self.head
        while temp:
                print(temp.data,"<-->",end=" ")
                temp=temp.next

obj=dll()
n1=Node(100)
obj.head=n1
n2=Node(200)
n2.previous=n1
n1.next=n2
obj.delete_end()
obj.display()


'''
'''
#       delete at position
class Node:
    def _init_(self,data):
        self.data=data
        self.previous=None
        self.next=None
class dll:
    def _init_(self):
        self.head=None
    def delete_pos(self,pos):
        temp=self.head.next
        prev=self.head
        for i in range(1,pos-1):
            temp=temp.next
            prev=prev.next
        prev.next=temp.next
        temp.next=None

        temp.next=None
    def display(self):
        if self.head is None:
            print("Empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,"<-->",end=" ")
                temp=temp.next
obj=dll()
n1=Node(100)
obj.head=n1
n2=Node(200)
n2.previous=n1
n1.next=n2
obj.delete_pos(2)
obj.display()


'''
'''
#circular linked list
class Node:
    def _init_(self,data):
        self.data=data
        self.next=None
class circular:
    def _init_(self):
        self.head=Node(None)
        self.tail=Node(None)
        self.head.next=self.tail
        self.tail.next=self.head


    def add(self,data):
        newNode=Node(data)
        if self.head.data is None:
            self.head=newNode
            self.tail=newNode
            newNode.next=self.head
        else:
            self.tail.next=newNode
            self.tail=newNode
            self.tail.next=self.head
    def display(self):
        current=self.head
        if self.head is None:
            print("List is Empty")
        else:
            print("Nodes of the Circular list:")
            print(current.data,"-->")
            while(current.next!=self.head):
                current=current.next
                print(current.data,"-->")     

class circularLinkedList:
    c1=circular()
    c1.add("S")
    c1.add("a")
    c1.add("s")
    c1.add("s")
    c1.display()
'''


