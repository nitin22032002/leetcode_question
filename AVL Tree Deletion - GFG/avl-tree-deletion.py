#User function Template for python3

''' structure of tree node:

class Node:
    def __init__(self,x):
        self.data=x
        self.left=None
        self.right=None
        self.height=1

'''
def max_height(root):
    height = 0
    if root.left:
        height = root.left.height
    if root.right and height < root.right.height:
        height = root.right.height
    return height

def get_balance(root):
    cost = 0
    if root.left:
        cost += root.left.height
    if root.right:
        cost -= root.right.height
    return cost

def update(root, value):
    if value:
        if not root:
            return value
        elif root.data > value.data:
            root.left = update(root.left, value)
        else:
            root.right = update(root.right, value)
    root.height = 1 + max_height(root)
    return root

def left_rotate(root):
    if not root.right:
        return None
    else:
        temp = root.right.left
        temp2 = root.right
        root.right.left = root
        root.right = None
        root.height = 1 + max_height(root)
        update(temp2, temp)
        return temp2

def right_rotate(root):
    if not root.left:
        return None
    else:
        temp = root.left.right
        temp2 = root.left
        root.left.right = root
        root.left = None
        root.height = 1 + max_height(root)
        update(temp2, temp)
        return temp2

def deleteNode(root, data):
    if not root:
        return None
    elif root.data == data:
        if root.right and root.left:
            temp = root.right
            while temp.left:
                temp = temp.left
            root.data = temp.data
            root.right = deleteNode(root.right, temp.data)
        elif root.right:
            temp = root.right
            del root
            return temp
        else:
            temp = root.left
            del root
            return temp
    elif root.data > data:
        root.left = deleteNode(root.left, data)
    else:
        root.right = deleteNode(root.right, data)
    root.height = 1 + max_height(root)
    cost = get_balance(root)
    if cost > 1:
        if get_balance(root.left) >= 0:
            root = right_rotate(root)
        else:
            root.left = left_rotate(root.left)
            root = right_rotate(root)
    elif cost < -1:
        if get_balance(root.right) <= 0:
            root = left_rotate(root)
        else:
            root.right = right_rotate(root.right)
            root = left_rotate(root)
    return root


#{ 
 # Driver Code Starts
#Initial Template for Python 3

from collections import deque

class Node:
    def __init__(self,x):
        self.data=x
        self.left=None
        self.right=None
        self.height=1

def setHeights(n):
    if not n:
        return 0
    n.height = 1 + max( setHeights(n.left) , setHeights(n.right) )
    return n.height

def buildTree(s):
    #Corner Case
    if(len(s)==0 or s[0]=="N"):           
        return None
        
    # Creating list of strings from input 
    # string after spliting by space
    ip=list(map(str,s.split()))
    
    # Create the root of the tree
    root=Node(int(ip[0]))                     
    size=0
    q=deque()
    
    # Push the root to the queue
    q.append(root)                            
    size=size+1 
    
    # Starting from the second element
    i=1                                       
    while(size>0 and i<len(ip)):
        # Get and remove the front of the queue
        currNode=q[0]
        q.popleft()
        size=size-1
        
        # Get the current node's value from the string
        currVal=ip[i]
        
        # If the left child is not null
        if(currVal!="N"):
            
            # Create the left child for the current node
            currNode.left=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.left)
            size=size+1
        # For the right child
        i=i+1
        if(i>=len(ip)):
            break
        currVal=ip[i]
        
        # If the right child is not null
        if(currVal!="N"):
            
            # Create the right child for the current node
            currNode.right=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.right)
            size=size+1
        i=i+1
    
    setHeights(root)
    return root

def isBST(n, lower, upper):
    if not n:
        return True
    
    if n.data <= lower or n.data >= upper:
        return False
    
    return isBST(n.left, lower, n.data) and isBST(n.right, n.data, upper)

def isBalanced(n):
    if not n:
        return (0,True)
    
    lHeight, l = isBalanced(n.left)
    rHeight, r = isBalanced(n.right)
    
    if abs( lHeight - rHeight ) > 1:
        return (0, False)
    
    return ( 1 + max( lHeight,rHeight  ) , l and r )

def isBalancedBST(root):
    if not isBST(root, -1000000000, 1000000000):
        print("BST voilated, inorder traversal :", end=' ')
    
    elif not isBalanced(root)[1]:
        print("Unbalanced BST, inorder traversal :", end=' ')
    
    else:
        return True
    
    return False

def printInorder(n):
    if not n:
        return
    printInorder(n.left)
    print(n.data, end=' ')
    printInorder(n.right)

if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        s = input()
        root = buildTree(s)
        
        n = int(input())
        ip = [ int(x) for x in input().split() ]
        
        for i in range(n):
            root = deleteNode( root, ip[i] )
            
            if not isBalancedBST(root):
                break
        
        if root is None:
            print("null")
        else:
            printInorder(root)
            print()

# } Driver Code Ends