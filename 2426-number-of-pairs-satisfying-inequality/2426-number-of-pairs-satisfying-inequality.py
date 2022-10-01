from sortedcontainers import SortedList
class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        arr=[]
        for i in range(len(nums1)):
            arr.append(nums1[i]-nums2[i])
        obj=SortedList()
        count=0
        for item in arr:
            count+=obj.bisect_right(item+diff)
            obj.add(item)
        return count