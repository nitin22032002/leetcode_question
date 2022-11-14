#User function Template for python3

class Solution:
    
    #Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self,W, wt, val, n):
        dp=[[0 for _ in range(n+1)] for __ in range(W+1)]
        for i in range(1,W+1):
            cost=0
            for j in range(1,n+1):
                if(wt[j-1]<=i):
                    cost=max(cost,(val[j-1]+dp[i-wt[j-1]][j-1]))
                dp[i][j]=cost
        return dp[W][n]

#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        W = int(input())
        val = list(map(int,input().strip().split()))
        wt = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.knapSack(W,wt,val,n))
# } Driver Code Ends