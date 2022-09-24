class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        d={0:1}
        s=0
        ans=0
        for item in nums:
            s+=item
            if(s-goal in d):
                ans+=d[s-goal]
            if(s in d):
                d[s]+=1
            else:
                d[s]=1
        return ans