from random import choice
class Solution:

    def __init__(self, nums: List[int]):
        self.d={}
        for i in range(len(nums)):
            if(nums[i] in self.d):
                self.d[nums[i]].append(i)
            else:
                self.d[nums[i]]=[i]
    def pick(self, target: int) -> int:
        return choice(self.d[target])


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)