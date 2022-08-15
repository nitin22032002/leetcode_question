class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor=0
        for i in range(len(nums)):
            xor^=nums[i]
        x1=0
        x2=0
        bit=0
        i=0
        while(xor&(1<<i)==0):
            bit+=1
            i+=1
        for item in nums:
            if(item&(1<<bit)==0):
                x1^=item
            else:
                x2^=item
        return x1,x2
        
        