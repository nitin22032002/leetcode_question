from typing import List
import sys

sys.setrecursionlimit(10**6)
from bisect import bisect_left
class Solution:
    def maximum_profit(self, n : int, intervals : List[List[int]]) -> int:
        intervals.sort()
        dp=[-1 for _ in range(n)]
        return self.get(intervals,0,dp)

    def get(self,interval,i,dp):
        if(i>=len(interval)):
            return 0
        elif(dp[i]==-1):
            j=bisect_left(interval,[interval[i][1],interval[i][1],0],i+1)
            ans=self.get(interval,j,dp)+interval[i][2]
            ans=max(ans,self.get(interval,i+1,dp))
            dp[i]=ans
        return dp[i]



#{ 
 # Driver Code Starts
class IntMatrix:
    def __init__(self) -> None:
        pass
    def Input(self,n,m):
        matrix=[]
        #matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix
    def Print(self,arr):
        for i in arr:
            for j in i:
                print(j,end=" ")
            print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        
        intervals=IntMatrix().Input(n, 3)
        
        obj = Solution()
        res = obj.maximum_profit(n, intervals)
        
        print(res)
        

# } Driver Code Ends