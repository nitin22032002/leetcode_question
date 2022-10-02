class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        dp=[[-1 for _ in range(n+1)] for __ in range(target+1)]
        return self.get(n,k,target,dp)
    def get(self,n,k,target,dp):
        if(n==0):
            if(target==0):
                return 1
            return 0
        elif(target<=0):
            return 0
        elif(dp[target][n]!=-1):
            return dp[target][n]
        else:
            ans=0
            for i in range(1,k+1):
                ans+=self.get(n-1,k,target-i,dp)
            dp[target][n]= (ans)%((10**9)+7)
            return dp[target][n]