# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        c,move=self.get(root)
        return move
    def get(self,root):
        if(root):
            coin=root.val
            c,move=self.get(root.left)
            coin+=c
            c,m=self.get(root.right)
            coin+=c
            move+=m
            if(coin<1):
                move+=(abs(coin)+1)
                return [coin-1,move]
            else:
                move+=coin-1
                return [coin-1,move]
        return [0,0]