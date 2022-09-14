# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.get(root,-(2**31)-1,(2**31))
    def get(self,root,min_val,max_val):
        if(root):
            if(root.val<=min_val or root.val>=max_val):
                return False
            return self.get(root.left,min_val,root.val) and self.get(root.right,root.val,max_val)
        return True
        