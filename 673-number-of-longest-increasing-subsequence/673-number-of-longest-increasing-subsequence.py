class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        d=[[0,0] for _ in range(len(nums))]
        ans=1
        for i in range(len(nums)):
            s=0
            for j in range(i):
                if(nums[i]>nums[j]):
                    s=max(s,d[j][0])
            d[i][0]=s+1
            ans=max(s+1,ans)
            for j in range(i):
                if(nums[i]>nums[j] and d[j][0]==s):
                    d[i][1]+=d[j][1]
            if(d[i][1]==0):
                d[i][1]=1
        res=0
        for i in range(len(nums)):
            if(d[i][0]==ans):
                res+=d[i][1]
        return res