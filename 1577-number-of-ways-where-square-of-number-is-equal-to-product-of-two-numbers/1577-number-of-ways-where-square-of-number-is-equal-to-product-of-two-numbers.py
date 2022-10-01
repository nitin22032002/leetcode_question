class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        d1={}
        d2={}
        for i in range(len(nums1)):
            if((nums1[i]*nums1[i]) in d1):
                d1[nums1[i]*nums1[i]]+=1
            else:
                d1[nums1[i]*nums1[i]]=1
        for i in range(len(nums2)):
            if((nums2[i]*nums2[i]) in d2):
                d2[nums2[i]*nums2[i]]+=1
            else:
                d2[nums2[i]*nums2[i]]=1
        ans=self.solve(nums1,d2)+self.solve(nums2,d1)
        return ans
    def solve(self,nums,d):
        ans=0
        for i in  range(len(nums)):
            for j in range(i+1,len(nums)):
                if(nums[i]*nums[j] in d):
                    ans+=d[nums[i]*nums[j]]
        return ans
        