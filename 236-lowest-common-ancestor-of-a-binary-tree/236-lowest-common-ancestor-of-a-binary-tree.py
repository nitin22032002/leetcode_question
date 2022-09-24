# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        i,ans=self.lca(root,p,q)
        return ans
    def lca(self,root,p,q):
        if(root):
            i,a=self.lca(root.left,p,q)
            if(a):
                return [0,a]
            j,a=self.lca(root.right,p,q)
            if(a):
                return [0,a]
            i+=j
            if(root==p):
                i+=1
            if(root==q):
                i+=1
            if(i==2):
                return [0,root]
            return [i,None]
        return [0,None]
        