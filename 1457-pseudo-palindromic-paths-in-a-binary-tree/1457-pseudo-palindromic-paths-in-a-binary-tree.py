# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        return self.get(root,0)
    def get(self,root,bit):
        if(root):    
            b=1<<root.val
            # print(b,bit)
            if(bit&b==0):
                bit|=b
            else:
                bit^=b
            ans=self.get(root.left,bit)+self.get(root.right,bit)
            # print(bit)
            if(root.left==None and root.right==None):
                isOdd=False
                for i in range(1,10):
                    b=1<<i
                    # print(b&bit)
                    if(b&bit!=0):
                        if(isOdd):
                            return 0
                        else:
                            isOdd=True
                ans+=1
            if(bit&b==0):
                bit|=b
            else:
                bit^=b
            return ans
        return 0