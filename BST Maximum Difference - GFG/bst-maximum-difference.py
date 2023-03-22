#User function Template for python3

'''
class Node:
    def __init__(self,val):
        self.data=val
        self.left=None
        self.right=None
'''

class Solution:
    def maxDifferenceBST(self,root, target):
        val=[None]
        ans=self.findCost(root,target,val)
        if(ans==-1):return -1
        sr=self.cost(val[0])
        sr[0]-=val[0].data
        sr[1]-=val[0].data
        # print(sr,ans)
        return max((ans-sr[0]),(ans-sr[1]))
    def findCost(self,root,target,val):
        if(root):
            if(target==root.data):
                val[0]=root
                return 0
            elif(target<root.data):
                ans=self.findCost(root.left,target,val)
                if(ans==-1):return -1
                return ans+root.data
            else:
                ans=self.findCost(root.right,target,val)
                if(ans==-1):return -1
                return ans+root.data
        return -1
    def cost(self,root):
        if(root):
            if(not root.left and not root.right):
                return [root.data,root.data]
            tem=[]
            if(root.left):
                tem+=self.cost(root.left)
            if(root.right):
                tem+=self.cost(root.right)
            return [max(tem)+root.data,min(tem)+root.data]
        return [1e9,1e9]


#{ 
 # Driver Code Starts
#Initial Template for Python 3
class Node:
    """ Class Node """
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None

class Tree:
    def createNode(self, data):
        return Node(data)
    
    def insert(self, node, data):
        if node is None:
            return self.createNode(data)
        else:
            if data < node.data:
                node.left = self.insert(node.left, data)
            else:
                node.right = self.insert(node.right, data)
            return node

    def traverseInorder(self, root):
        if root is not None:
            print(root.data, end= " ")
            self.traverseInorder(root.left)
            self.traverseInorder(root.right)
    
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        n=int(input())
        arr = input().strip().split()
        root = None
        tree = Tree()
        root = tree.insert(root, int(arr[0]))
        for j in range(1, n):
            root = tree.insert(root, int(arr[j]))
        #tree.traverseInorder(root)
        target = int(input())
        
        res = Solution().maxDifferenceBST(root, target)
        print(res)

# } Driver Code Ends