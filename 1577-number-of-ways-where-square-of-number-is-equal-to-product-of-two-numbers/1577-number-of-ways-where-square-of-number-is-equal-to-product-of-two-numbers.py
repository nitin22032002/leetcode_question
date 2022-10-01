class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        d1={}
        d2={}
        for i in range(len(nums1)):
            if(nums1[i] in d1):
                d1[nums1[i]].append(i)
            else:
                d1[nums1[i]]=[i]
        for i in range(len(nums2)):
            if(nums2[i] in d2):
                d2[nums2[i]].append(i)
            else:
                d2[nums2[i]]=[i]
        ans=self.solve(nums1,nums2,d2)+self.solve(nums2,nums1,d1)
        return ans
    def solve(self,nums1,nums2,d):
        ans=0
        for item in nums1:
            target=item*item
            for i in range(len(nums2)):
                if(target%nums2[i]==0 and (target//nums2[i]) in d):
                    arr=d[target//nums2[i]]
                    ans+=(len(arr)-self.upperBound(arr,i+1))
        return ans
    def upperBound(self,arr,target):
        end=len(arr)-1
        start=0
        while(start<end-1):
            mid=(start+end)//2
            if(arr[mid]<target):
                start=mid
            else:
                end=mid
        if(arr[start]>=target):
            return start
        elif(arr[end]>=target):
            return end
        return len(arr)
        