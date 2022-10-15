class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        s=sum(nums)
        t=0
        i=0
        ans=[]
        while(i<len(nums)):
            s-=nums[i]
            res=((i)*nums[i]-t)
            res+=(s-(len(nums)-i-1)*nums[i])
            ans.append(res)
            t+=nums[i]
            i+=1
        return ans