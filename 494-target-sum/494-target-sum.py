class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        return self.get(nums,0,target,{})
    def get(self,nums,curr,target,dp):
        if(curr>=len(nums)):
            if(target==0):
                return 1
            return 0
        elif((curr,target) in dp):
            return dp[(curr,target)]
        else:
            dp[(curr,target)]= self.get(nums,curr+1,target+nums[curr],dp)+self.get(nums,curr+1,target-nums[curr],dp)
            return dp[(curr,target)]