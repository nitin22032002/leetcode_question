#User function Template for python3

class Solution:
    
    #Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self,W, wt, val, n):
        dp=[[-1 for _ in range(W+1)] for __ in range(n)]
        return self.get(W,wt,val,0,dp)
    def get(self,w,wt,val,i,dp):
        if(i>=len(wt)):
            return 0
        elif(dp[i][w]==-1):
            ans=0
            if(wt[i]<=w):
                ans=(val[i]+self.get(w-wt[i],wt,val,i+1,dp))
            ans=max(ans,self.get(w,wt,val,i+1,dp))
            dp[i][w]=ans
        return dp[i][w]


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