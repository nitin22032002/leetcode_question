#User function Template for python3

class Solution:
    def nCr(self, n, r):
        dp=[[0 for _ in range(r+1)] for __ in range(n+1)]
        mod=((10**9)+7)
        for i in range(n+1):
            dp[i][0]=1
        for i in range(1,r+1):
            for j in range(0,n+1):
                if(j<i):
                    continue
                dp[j][i]=(dp[j-1][i-1]+dp[j-1][i])%mod
        return dp[n][r]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, r = [int(x) for x in input().split()]
        
        ob = Solution()
        print(ob.nCr(n, r))
# } Driver Code Ends