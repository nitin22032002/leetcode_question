class Solution:
    def getMoneyAmount(self, n: int) -> int:
        return self.get(1,n,[[-1 for _ in range(n+1)] for __ in range(n+1)])
    def get(self,start,end,dp):
        if(start>=end):
            return 0
        elif(end-start==1):
            return start
        elif(end-start==2):
            return start+1
        elif(dp[start][end]!=-1):
            return dp[start][end]
        else:
            ans=10**9
            for i in range(start,end+1):
                ans=min(i+max(self.get(start,i-1,dp),self.get(i+1,end,dp)),ans)
            dp[start][end]=ans
            return ans