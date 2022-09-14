class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_or=0
        for item in nums:
            max_or|=item
        return self.get(nums,0,max_or,0)
    def get(self,nums,i,max_or,curr_or):
        if(i>=len(nums)):
            if(curr_or==max_or):
                return 1
            return 0
        else:
            return self.get(nums,i+1,max_or,curr_or)+self.get(nums,i+1,max_or,curr_or|nums[i])