#User function Template for python3

from typing import List
from queue import PriorityQueue
class Solution:
    def shortestPath(self, n : int, m : int, edges : List[List[int]]) -> List[int]:
        visited=[-1 for _ in range(n)]
        graph=[[] for _ in range(n)]
        for a,b,c in edges:
            graph[a].append([b,c])
        obj=PriorityQueue()
        obj.put([0,0])
        visited[0]=0
        while(not obj.empty()):
            cost,node=obj.get()
            for a,b in graph[node]:
                if(visited[a]==-1 or visited[a]>b+cost):
                    visited[a]=cost+b
                    obj.put([cost+b,a])
        return visited
        


#{ 
 # Driver Code Starts

#Initial Template for Python 3

from typing import List




class IntMatrix:
    def __init__(self) -> None:
        pass
    def Input(self,n,m):
        matrix=[]
        #matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix
    def Print(self,arr):
        for i in arr:
            for j in i:
                print(j,end=" ")
            print()



class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n,m=map(int,input().split())
        
        
        edges=IntMatrix().Input(m, 3)
        
        obj = Solution()
        res = obj.shortestPath(n, m, edges)
        
        IntArray().Print(res)
# } Driver Code Ends