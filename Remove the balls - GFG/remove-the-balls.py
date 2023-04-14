from typing import List


class Solution:
    def finLength(self, N : int, color : List[int], radius : List[int]) -> int:
        stack=[]
        for i in range(N):
            if(len(stack)==0 or color[i]!=color[stack[-1]] or radius[i]!=radius[stack[-1]]):
                stack.append(i)
            else:
                stack.pop()
        return len(stack)
        



#{ 
 # Driver Code Starts
class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        N = int(input())
        
        
        color=IntArray().Input(N)
        
        
        radius=IntArray().Input(N)
        
        obj = Solution()
        res = obj.finLength(N, color, radius)
        
        print(res)
        

# } Driver Code Ends