from queue import PriorityQueue
class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        obj=PriorityQueue()
        arr=[[efficiency[i],speed[i]] for i in range(n)]
        arr.sort(reverse=True)
        ts=0
        ans=0
        INT_MAX=(10**9)+7
        for eff,curr_speed in arr:
            obj.put(curr_speed)
            if(obj.qsize()<=k):
                ts+=curr_speed
            else:
                ts+=(curr_speed-obj.get())
            ans=max(ans,ts*eff)
        return ans%INT_MAX