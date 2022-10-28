class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        r=sum(nums)
        l=0
        for i in range(len(nums)):
            r-=nums[i]
            if(r==l):
                return i
            l+=nums[i]
        return -1