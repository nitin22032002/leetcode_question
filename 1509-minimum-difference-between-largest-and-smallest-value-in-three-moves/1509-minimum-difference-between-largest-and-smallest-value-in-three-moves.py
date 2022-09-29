class Solution:
    def minDifference(self, nums: List[int]) -> int:
        nums.sort()
        return self.get(nums,3,0,len(nums)-1)
    def get(self,nums,moves,i,j):
        if(i>=j):
            return 0
        elif(moves==0):
            return nums[j]-nums[i]
        else:
            return min(self.get(nums,moves-1,i+1,j),self.get(nums,moves-1,i,j-1))
        
        