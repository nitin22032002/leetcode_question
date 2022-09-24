class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp=[[-1001 for _ in range(2)] for __ in range(len(prices))]
        return self.get(prices,0,0,dp)
    def get(self,prices,curr,state,dp):
        if(curr>=len(prices)):
            return 0
        elif(dp[curr][state]!=-1001):
            return dp[curr][state]
        else:
            if(state==0):
                dp[curr][state]=max(self.get(prices,curr+1,1,dp)-prices[curr],self.get(prices,curr+1,0,dp))
            else:
                dp[curr][state]=max(self.get(prices,curr+2,0,dp)+prices[curr],self.get(prices,curr+1,state,dp))
            return dp[curr][state]