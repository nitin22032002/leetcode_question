#User function Template for python3
from queue import PriorityQueue
from typing import List
class Solution:
    def minimumCost(self, flights: List[List[int]], n : int, k : int) -> int:
        obj=PriorityQueue()
        graph=[[] for _ in range(n)]
        for item in flights:
            a,b,cost=item
            graph[a-1].append([b-1,cost])
        # print(graph)
        visited=[-1 for _ in range(n)]
        visited[k-1]=0
        obj.put([k-1,0])
        while(not obj.empty()):
            i,cost=obj.get()
            # print((i,cost))
            for item in graph[i]:
                b,c=item
                if(visited[b]==-1 or visited[b]>c+cost):
                    visited[b]=c+cost
                    obj.put([b,c+cost])
        # print(visited)
        if(min(visited)==-1):
            return -1
        return max(visited)
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

    
if __name__=="__main__":
    T = int(input())
    for t in range(T):
        
        n = int(input())
        k = int(input())
        m = int(input())
        flights = []
        for i in range(m):
            u, v, wt = map(int, input().strip().split())
            flights.append([u, v, wt])
        obj = Solution()
        ans = obj.minimumCost(flights, n, k)
        print(ans)
            

# } Driver Code Ends