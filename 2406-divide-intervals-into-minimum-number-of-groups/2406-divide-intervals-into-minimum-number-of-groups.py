from queue import PriorityQueue
class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        # print(intervals)
        obj=PriorityQueue()
        ans=0
        for item in intervals:
            if(obj.qsize()==0):
                obj.put(item[1])
                ans+=1
            else:
                a=obj.get()
                if(item[0]<=a):
                    ans+=1
                    obj.put(a)
                    obj.put(item[1])
                else:
                    obj.put(item[1])
        return ans
                        