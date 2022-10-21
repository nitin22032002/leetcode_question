class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        a1=self.kandles(nums)
        for i in range(len(nums)):
            nums[i]*=-1
        a2=self.kandles(nums)
        return max(a1,a2)
    def kandles(self,nums):
        if(max(nums)<=0):
            return 0
        else:
            s=0
            ans=0
            for item in nums:
                s+=item
                # print(s)
                if(s<0):
                    s=0
                ans=max(ans,s)
            return ans