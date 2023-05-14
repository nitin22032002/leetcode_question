from typing import List

class Solution:
    def findMaxSubsetSum(self, N : int, A : List[int]) -> int:
        dp=[[0,0] for _ in range(N+1)]
        for i in range(N):
            dp[i+1][0]=dp[i][1]
            dp[i+1][1]=max(dp[i][1],dp[i][0])+A[i]
        return max(dp[N])
        



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
        
        
        A=IntArray().Input(N)
        
        obj = Solution()
        res = obj.findMaxSubsetSum(N, A)
        
        print(res)
        

# } Driver Code Ends