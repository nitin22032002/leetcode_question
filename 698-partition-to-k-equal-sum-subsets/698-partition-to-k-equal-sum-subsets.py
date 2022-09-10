class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total=sum(nums)
        if(total%k!=0):
            return False
        target=total//k
        arr=[target for _ in range(k)]
        # print(arr)
        return self.get(nums,0,target,0,k,target,{})
    def get(self,nums,i,target,bit,k,s,d):
        if(k==0):
            return bit==((2**len(nums))-1)
        elif((bit,k) in d):
            return d[(bit,k)]
        elif(target==0):
            d[(bit,k)] =self.get(nums,0,s,bit,k-1,s,d)
        elif(i>=len(nums)):
            return False
        elif((1<<i)&bit!=0):
            status=self.get(nums,i+1,target,bit,k,s,d)
            d[(bit,k)]= status
        else:
            b=1<<i
            status=False
            if(target-nums[i]>=0):
                status= self.get(nums,i+1,target-nums[i],bit|b,k,s,d)
            if(status):
                d[(bit,k)]= status
                return status
            status=self.get(nums,i+1,target,bit,k,s,d)
            d[(bit,k)]= status
        return d[(bit,k)]