from sortedcontainers import SortedList
class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        obj=SortedList()
        s=0
        obj.add(0)
        ans=0
        for item in nums:
            s+=item
            # print(obj)
            # print(s-lower,s-upper)
            l1=obj.bisect_right(s-lower)
            l1-=1
            l2=obj.bisect_left(s-upper)
            # print((l1,l2))
            if(l1>=l2):
                ans+=((l1-l2)+1)
            obj.add(s)
        return ans
    