# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        return self.get(root,targetSum)
    def get(self,root,target):
        if(root):
            if(not root.left and not root.right):
                return (target-root.val)==0
            return self.get(root.left,target-root.val) or self.get(root.right,target-root.val)
        return False