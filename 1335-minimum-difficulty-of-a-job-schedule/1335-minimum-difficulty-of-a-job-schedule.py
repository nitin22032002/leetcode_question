class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        if(len(jobDifficulty)<d):
            return -1
        ans=self.get(jobDifficulty,0,d,{})
        if(ans>=10**9):
            return -1
        return ans
    def get(self,arr,i,d,dp):
        # print((i,d))
        if(d==0 and i>=len(arr)):
            return 0
        elif((i,d) in dp):
            return dp[(i,d)]
        elif(d==1):
            dp[(i,d)]= max(arr[i:])
        elif(d==(len(arr)-i)):
            dp[(i,d)]= sum(arr[i:])
        else:
            ans=10**9
            m=-1
            for j in range(i,(len(arr)-d+1)):
                m=max(m,arr[j])
                ans=min(ans,self.get(arr,j+1,d-1,dp)+m)
            dp[(i,d)]=ans
        return dp[(i,d)]