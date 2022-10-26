class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        d={0:-1}
        s=0
        for i,item in enumerate(nums):
            s+=item
            # print(s)
            if(s%k in d):
                if(i-d[s%k]>=2):
                    return True
            else:
                d[s%k]=i
        return False
        