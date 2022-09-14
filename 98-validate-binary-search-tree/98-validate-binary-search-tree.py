# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        ans=[True]
        self.INT=-pow(2,31)-1
        self.get(root,ans)
        return ans[0]
    def get(self,root,g):
        if(root and g[0]):
            a=self.get(root.left,g)
            if(a[0]!=self.INT):
                if(root.val<=a[1]):
                    g[0]=False
            b=self.get(root.right,g)
            if(b[0]!=self.INT):
                if(root.val>=b[0]):
                    g[0]=False
            if(a[0]==self.INT):
                a[0]=root.val
            if(b[1]==self.INT):
                b[1]=root.val
            return [a[0],b[1]]
        return [self.INT,self.INT]