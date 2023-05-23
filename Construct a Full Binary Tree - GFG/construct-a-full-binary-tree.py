#User function Template for python3
class Node:
    def __init__(self,val):
        self.data=val
        self.left=self.right=None
from math import log,ceil
class Solution:
    def constructBinaryTree(self, pre, preMirror, size):
        if(len(pre)==1):
            return Node(pre[0])
        h=ceil(log(len(pre))/log(2))
        self.i=0
        return self.get(pre,h)
    def get(self,pre,h):
        if(h==0):
            return None
        root=Node(pre[self.i])
        self.i+=1
        root.left=self.get(pre,h-1)
        root.right=self.get(pre,h-1)
        return root
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    
    def printInorder(node):
        if node == None:
            return
        printInorder(node.left)
        print(node.data, end = " ")
        printInorder(node.right)
        
    test_cases = int(input())
    for _ in range (test_cases):
        N = int(input())
        pre = list(map(int, input().split()))
        preMirror = list(map(int, input().split()))
        res = Solution().constructBinaryTree(pre, preMirror, N)
        if printInorder(res) != None:
            print(printInorder(res)[:len(printInorder(res))-2])
        print()
# } Driver Code Ends