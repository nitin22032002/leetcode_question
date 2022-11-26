class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        arr=[]
        for i in range(len(startTime)):
            arr.append([startTime[i],endTime[i],profit[i]])
        arr.sort()
        dp=[-1 for _ in range(len(arr))]
        return self.get(arr,0,dp)
    def get(self,arr,i,dp):
        if(i>=len(arr)):
            return 0
        elif(dp[i]!=-1):
            return dp[i]
        else:
            j=bisect_left(arr,[arr[i][1],arr[i][0],-1])
            ans=max(arr[i][2]+self.get(arr,j,dp),self.get(arr,i+1,dp))
            dp[i]=ans
            return ans