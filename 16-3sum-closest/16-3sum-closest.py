class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        result=100000
        for i in range(len(nums)):
            if(i!=0 and nums[i]==nums[i-1]):continue
            j=i+1
            k=len(nums)-1
            while(j<k):
                # print(i,j,k)
                s=nums[i]+nums[j]+nums[k]
                if(abs(target-s)<abs(target-result)):
                    result=s
                else:
                    pass
                if(s==target):
                    return target
                elif(s>target):
                    k-=1
                else:
                    j+=1
        return result
   