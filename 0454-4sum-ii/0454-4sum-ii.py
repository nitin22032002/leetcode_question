class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        d1={}
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                p=nums1[i]+nums2[j]
                if(p in d1):
                    d1[p]+=1
                else:
                    d1[p]=1
        d2={}
        for i in range(len(nums3)):
            for j in range(len(nums4)):
                p=nums3[i]+nums4[j]
                if(p in d2):
                    d2[p]+=1
                else:
                    d2[p]=1
        ans=0
        for item in d1:
            if(-item in d2):
                ans+=(d1[item]*d2[-item])
        return ans
        