class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        dp=[[-1,-1] for _ in range(len(prices))]
        return self.get(prices,0,0,fee,dp)
    def get(self,price,i,state,fee,dp):
        if(i>=len(price)):
            return 0
        elif(dp[i][state]==-1):
            if(state==0):
                ans=max(self.get(price,i+1,state,fee,dp),self.get(price,i+1,1,fee,dp)-price[i]-fee)
            else:
                ans=max(self.get(price,i+1,state,fee,dp),self.get(price,i+1,0,fee,dp)+price[i])
            dp[i][state]=ans
        return dp[i][state]