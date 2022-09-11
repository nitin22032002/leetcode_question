# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.root=set()
        self.recover(root,0)
    def recover(self,root,i):
        if(root):
            root.val=i
            self.root.add(i)
            if(root.left):
                self.recover(root.left,(2*root.val)+1)
            if(root.right):
                self.recover(root.right,(2*root.val)+2)

    def find(self, target: int) -> bool:
        return target in self.root
    
            


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)