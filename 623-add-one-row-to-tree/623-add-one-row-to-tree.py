# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        return self.get(root,1,depth,val,True)
    def get(self,root,d,req,val,state):
        if(root):
            if(req==d):
                node=TreeNode(val)
                if(state):
                    node.left=root
                else:
                    node.right=root
                return node
            else:
                root.left=self.get(root.left,d+1,req,val,True)
                root.right=self.get(root.right,d+1,req,val,False)
                return root
        else:
            if(d==req):
                return TreeNode(val)