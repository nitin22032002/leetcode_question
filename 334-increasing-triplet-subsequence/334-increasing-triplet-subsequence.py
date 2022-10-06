class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if(len(nums)<=2):
            return False
        maxArr=[]
        for i in range(len(nums)-1,-1,-1):
            if(len(maxArr)==0):
                maxArr.append(nums[i])
            else:
                maxArr.append(max(nums[i],maxArr[-1]))
        maxArr.reverse()
        minVal=nums[0]
        i=1
        while(i<len(nums)-1):
            l1=minVal
            l2=maxArr[i+1]
            if(nums[i]>l1 and nums[i]<l2):
                return True
            minVal=min(minVal,nums[i])
            i+=1
        return False
        