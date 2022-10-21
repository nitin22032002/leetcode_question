class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        i=0
        j=0
        d=set()
        while(j<len(nums)):
            if((j-i)<=k):
                if(nums[j] in d):
                    return True
                d.add(nums[j])
                j+=1
            else:
                d.remove(nums[i])
                i+=1
        return False