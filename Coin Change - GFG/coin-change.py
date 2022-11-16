#User function Template for python3

class Solution:
    def count(self, coins, N, Sum):
        dp=[[-1 for _ in range(N)] for __ in range(Sum+1)]
        return self.get(coins,0,Sum,dp)
    def get(self,coins,i,Sum,dp):
        if(Sum==0):
            return 1
        elif(i>=len(coins)):
            return 0
        elif(dp[Sum][i]==-1):
            ans=0
            for j in range(i,len(coins)):
                if(coins[j]>Sum):
                    break
                ans+=self.get(coins,j,Sum-coins[j],dp)
            dp[Sum][i]=ans
        return dp[Sum][i]



#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        sum,N = list(map(int, input().strip().split()))
        coins = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.count(coins,N,sum))

# } Driver Code Ends