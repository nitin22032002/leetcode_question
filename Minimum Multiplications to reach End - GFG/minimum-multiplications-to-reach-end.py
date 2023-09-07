#User function Template for python3

from typing import List
 
from queue import Queue
class Solution:
    
    def minimumMultiplications(self, arr : List[int], start : int, end : int) -> int:
        mod=int(1e5)
        obj=Queue()
        visited=[False]*(mod)
        obj.put([start,0])
        visited[start]=0
        while(not obj.empty()):
            node,cost=obj.get()
            if(node==end):return cost
            for item in arr:
                val=(item*node)%mod
                if(not visited[val]):
                    obj.put([val,cost+1])
                    visited[val]=True
        return -1        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    for _ in range(int(input())):
        n = int(input())
        arr = [int(x) for x in input().strip().split()]
        start, end = list(map(int,input().split()))
        obj=Solution()
        print(obj.minimumMultiplications(arr, start, end))
# } Driver Code Ends