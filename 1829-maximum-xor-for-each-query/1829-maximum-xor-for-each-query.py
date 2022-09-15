class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        xor=nums[0]
        for i in range(1,len(nums)):
            xor^=nums[i]
        j=len(nums)-1
        ans=[]
        while(j>=0):
            k=0
            for i in range(maximumBit):
                b=1<<i
                if(xor&b==0):
                    k|=b
            ans.append(k)
            xor^=nums[j]
            j-=1
        return ans