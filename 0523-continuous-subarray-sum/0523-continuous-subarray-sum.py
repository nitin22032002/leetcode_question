class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        d={0:-1}
        s=0
        for i,item in enumerate(nums):
            s+=item
            # print(s)
            if(i-d.get(s%k,i)>=2):
                return True
            elif(i!=0 and s%k==0):
                return True
            elif(s%k not in d):
                d[s%k]=i
        return False
        