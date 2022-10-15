from queue import PriorityQueue
class Solution:
    def halveArray(self, nums: List[int]) -> int:
        d=PriorityQueue()
        s=0
        for item in nums:
            d.put(-item)
            s+=item
        t=s
        ans=0
        while(s>(t/2)):
            top=d.get()
            ans+=1
            s-=((-top)/2)
            d.put(top/2)
        return ans