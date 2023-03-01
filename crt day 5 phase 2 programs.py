'''
#Binary tree implementation
class BinaryTreeNode:
    def __init__(self,data):
        self.data=data
        self.leftChild=None
        self.rightChild=None
node1=BinaryTreeNode(50)
node2=BinaryTreeNode(20)
node3=BinaryTreeNode(45)
node4=BinaryTreeNode(11)
node5=BinaryTreeNode(15)
node6=BinaryTreeNode(30)
node7=BinaryTreeNode(78)
node1.leftChild=node2
node1.rightChild=node3
node2.leftChild=node4
node2.rightChild=node5
node3.leftChild=node6
node3.rightChild=node7
print("The root node is: ")
print(node1.data)
print("left child of the node is: ")
print(node1.leftChild.data)
print("right child of the  nodeis: ")
print(node1.rightChild.data)
print("Node is: ")
print(node2.data)
print("left child of the node is: ")
print(node2.leafChild.data)
print("right child of the node is: ")
print(node2.rightChild.data)
'''

'''
#inorder,preorder,postorder
class Node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.val=key
def printInorder(root):
    if root:
        #First recur on left node
        printInorder(root.left)
        #then print the data of node
        print(root.val,end=" ")
        #now recur on right child
        printInorder(root.right)
def printPostorder(root):
    if root:
        #First recur on left child
        printPostorder(root.left)
        #now recur on right child
        printPostorder(root.right)
        #now print the data of node
        print(root.val,end=" ")
def printPreorder(root):
    if root:
        #First print the data of the node
        print(root.val,end=' ')
        #then recur on left child
        printPreorder(root.left)
        #next recur the right child
        printPreorder(root.right)
root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right=Node(5)
print("PRE-ORDER: ")
printPreorder(root)
print("\n INORDER: ")
printInorder(root)
print("\n POST-ORDER: ")
printPostorder(root)
'''
'''
#binary search tree
#1st 80,10,50,16,45,0,92,73,44
#2nd 200,25,5,10,15,-10.-30,61,97,-88,-55,77
#3rd 54321,12345,-1,-2,-3,-4,-5,0

#1st
             50
            /  \
          44    80
          / \   / \
         10  45 73  92
         / \         
        0  16       
 
#2nd   
              -10
           /         \
        -55          25
       /   \       /    \
     -88  -30    10     97
                /  \   /  \
               5   15 77 200      
                      /
                     61

#3rd [-5,-4,-3,-2,-1,0,12345,54321]
                0
               /  \
              -4    54321
              / \     /
            -5 -2    12345
               / \
              -3 -1
'''

'''
#Bst-INSERTION
class Node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.val=key

#a new node with the given key

def insert(root,key):
    if root is None:
        return Node(key)
    else:
        if root.val == key:
            return root
        elif root.val < key:
            root.right = insert(root.right,key)
        else:
            root.left = insert(root.left,key)
    return root
#Inorder-traversal
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)
#     50
#    /  \
#  30    70
# /  \   / \
#20  40 60 80
r = Node(50)
r = insert(r, 30)
r = insert(r, 20)
r = insert(r, 40)
r = insert(r, 70)
r = insert(r, 60)
r = insert(r, 80)
inorder(r)
'''


#
