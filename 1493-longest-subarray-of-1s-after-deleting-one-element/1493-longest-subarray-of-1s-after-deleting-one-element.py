class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # a=[]
        i=0
        ans=0
        zero=False
        c=0
        isDone=False
        while(i<len(nums)):
            t=0
            while(i<len(nums) and nums[i]==1):
                t+=1
                i+=1
            ans=max(ans,c+t)
            c=t
            isDone=False
            k=0
            while(i<len(nums) and nums[i]==0):
                k+=1
                zero=True
                i+=1
            if(k!=1 or isDone):
                c=0
            else:
                isDone=True
        if(not zero):
            ans-=1
        return ans
            