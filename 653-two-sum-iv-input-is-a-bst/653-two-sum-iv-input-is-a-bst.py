# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        return self.get(root,root,k)
    def get(self,root,Par,k):
        if(root):
            if(self.isExist(Par,root,k-root.val)):
                return True
            return self.get(root.left,Par,k) or self.get(root.right,Par,k)
        return False
    def isExist(self,root,notR,target):
        if(root):
            if(root.val==target and root!=notR):
                return True
            elif(root.val<target):
                return self.isExist(root.right,notR,target)
            else:
                return self.isExist(root.left,notR,target)
        return False