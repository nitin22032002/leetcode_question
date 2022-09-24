# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans=self.get(root,targetSum)
        for item in ans:
            item.reverse()
        return ans
    def get(self,root,target):
        if(root):
            if(not root.left and not root.right):
                if(root.val==target):
                    return [[root.val]]
                return []
            ans=self.get(root.left,target-root.val)
            ans+=self.get(root.right,target-root.val)
            for item in ans:
                item.append(root.val)
            return ans
        return []