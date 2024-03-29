'''
# node class:

class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

'''

class Solution:
    def ladoos(self, root, home, k):
        self.ans=0
        self.get(root,home,k)
        return self.ans
    def get(self,root,home,k):
        if(root):
            if(root.data==home):
                x=self.cost(root,k)
                self.ans+=x
                # print(x,root.data)
                return 1
            else:
                l=self.get(root.left,home,k)
                if(l==k):
                    # print(root.data)
                    self.ans+=root.data
                    return -1
                elif(l!=-1 and l<k):
                    self.ans+=self.cost(root.right,k-l-1)+root.data
                    return l+1
                else:
                    l=self.get(root.right,home,k)
                    if(l==k):
                        self.ans+=root.data
                        return -1
                    elif(l!=-1 and l<k):
                        self.ans+=self.cost(root.left,k-l-1)+root.data
                        return l+1
                    return -1
        return -1
    def cost(self,root,k):
        if(root and k!=-1):
            return self.cost(root.left,k-1)+self.cost(root.right,k-1)+root.data
        return 0




#{ 
 # Driver Code Starts
#driver code:
from collections import deque

# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

# Function to Build Tree   
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
    return root

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        line=input()
        root=buildTree(line)
        line=input().strip().split()
        home=int(line[0])
        k=int(line[1])
        obj = Solution();
        print(obj.ladoos(root,home,k))


# } Driver Code Ends