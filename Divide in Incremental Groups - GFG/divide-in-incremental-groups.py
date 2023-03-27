#User function Template for python3

class Solution:
    def countWaystoDivide(self, N, K):
        dp=[[[-1 for _ in range(K+1)] for __ in range(N+1)] for ___ in range(N+1)]
        return self.get(N,1,K,dp)
    def get(self,N,prv,k,dp):
        if(k==0):
            if(N==0):
                return 1
            return 0
        elif(N<=0 or prv>N):
            return 0
        elif(dp[N][prv][k]!=-1):
            return dp[N][prv][k]
        else:
            ans=0
            for i in range(prv,N+1):
                ans+=self.get(N-i,i,k-1,dp)
            dp[N][prv][k]=ans
            return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(1000000)

if __name__ == '__main__':
    
    T = int(input())
    while T > 0: 
        N =int(input())
        K=int(input())
        ob = Solution()
        print(ob.countWaystoDivide(N,K))
        
        T -= 1
# } Driver Code Ends