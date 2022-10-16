class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        sumEven=0
        sumOdd=0
        evenSum=0
        oddSum=0
        for i in range(len(nums)-1,-1,-1):
            if(i%2==0):
                evenSum+=nums[i]
            else:
                oddSum+=nums[i]
        i=0
        ans=0
        while(i<len(nums)):
            if(i%2==0):
                evenSum-=nums[i]
            else:
                oddSum-=nums[i]
            if(oddSum+sumEven==evenSum+sumOdd):
                ans+=1
            if(i%2==0):
                sumEven+=nums[i]
            else:
                sumOdd+=nums[i]
            i+=1
        return ans