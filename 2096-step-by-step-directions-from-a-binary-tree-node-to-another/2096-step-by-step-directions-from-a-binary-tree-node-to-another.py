# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        lca=self.lca(root,startValue,destValue)
        d=self.findDepth(lca,startValue)
        path=self.path(lca,destValue)
        if(path=="r"):
            path=""
        ans=("U"*(d-1))+path
        return ans
    def lca(self,root,p,q):
        if(root):
            if(p==root.val or q==root.val):
                return root
            left=self.lca(root.left,p,q)
            right=self.lca(root.right,p,q)
            if(not left):
                return right
            elif(not right):
                return left
            return root
        return None
    def findDepth(self,root,t):
        if(root):
            # print(root.val,t)
            if(root.val==t):
                return 1
            a=self.findDepth(root.left,t)
            a+=self.findDepth(root.right,t)
            if(a>=1):
                return a+1
        return 0
    def path(self,root,t):
        if(root):
            if(root.val==t):
                return "r"
            a=self.path(root.left,t)
            if(a=="r"):
                return "L"
            elif(a!=""):
                return "L"+a
            a=self.path(root.right,t)
            if(a=="r"):
                return "R"
            elif(a!=""):
                return "R"+a
        return ""