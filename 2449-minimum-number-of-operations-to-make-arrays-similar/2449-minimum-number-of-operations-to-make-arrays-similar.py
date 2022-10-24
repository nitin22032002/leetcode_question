class Solution:
    def makeSimilar(self, nums: List[int], target: List[int]) -> int:
        nums.sort(key=lambda x:[x%2,x])
        target.sort(key=lambda x:[x%2,x])
        ans=0
        for i in range(len(target)):
            ans+=abs(nums[i]-target[i])//2
        return ans//2
        