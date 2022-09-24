# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        ans=[]
        self.get(root,set(to_delete),ans,True)
        return ans
    def get(self,root,to_delete,ans,status):
        if(root):
            if(root.val in to_delete):
                self.get(root.left,to_delete,ans,True)
                self.get(root.right,to_delete,ans,True)
                return None
            else:
                root.left=self.get(root.left,to_delete,ans,False)
                root.right=self.get(root.right,to_delete,ans,False)
                if(status):
                    ans.append(root)
                return root
        return None
            