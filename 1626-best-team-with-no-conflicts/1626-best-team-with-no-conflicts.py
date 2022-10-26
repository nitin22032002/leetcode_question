class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        arr=[[ages[i],scores[i]] for i in range(len(ages))]
        arr.sort()
        dp=[[-1 for _ in range(len(ages)+1)] for __ in range(len(ages))]
        return self.get(arr,-1,0,dp)
    def get(self,arr,prv,i,dp):
        if(i>=len(arr)):
            return 0
        elif(dp[i][prv]!=-1):
            return dp[i][prv]
        else:
            not_take=self.get(arr,prv,i+1,dp)
            take=0
            if(prv==-1 or arr[prv][1]<=arr[i][1]):
                take=arr[i][1]+self.get(arr,i,i+1,dp)
            ans=max(take,not_take)
            dp[i][prv]=ans
            return ans