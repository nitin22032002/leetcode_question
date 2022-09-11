class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        m=nums[-1]
        bits=0
        while(m!=0):
            bits+=1
            m//=2
        arr=[0 for _ in range(max(m,maximumBit))]
        for item in nums:
            for i in range(len(arr)):
                b=1<<i
                if(b&item!=0):
                    arr[i]+=1
        ans=[0 for _ in range(len(nums))]
        i=0
        j=len(nums)-1
        while(j>=0):
            # print(arr)
            res=0
            for k in range(maximumBit):
                if(arr[k]%2==0):
                    b=1<<k
                    res|=b
            ans[i]=res
            for k in range(len(arr)):
                b=1<<k
                if(b&nums[j]!=0):
                    arr[k]-=1
            j-=1
            i+=1
        return ans
        