#User function Template for python3

class Solution:
    def count(self, coins, N, Sum):
        dp=[0 for _ in range(Sum+1)]
        dp[0]=1
        coins.sort()
        for i in range(len(coins)):
            for j in range(coins[i],Sum+1):
                dp[j]+=dp[j-coins[i]]
        return dp[-1] 



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