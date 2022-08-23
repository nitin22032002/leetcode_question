class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for i in range(len(nums)):
            nums[i]=str(nums[i])
        nums.sort(reverse=True)
        i=0
        while(i<len(nums)):
            j=i+1
            while(j<len(nums)):
                if(int(nums[i]+nums[j])<int(nums[j]+nums[i])):
                    nums[i],nums[j]=nums[j],nums[i]
                j+=1
            i+=1
        return str(int("".join(nums)))
        