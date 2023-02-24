#User function Template for python3
from queue import PriorityQueue
class Solution:
    def shortestPath(self, n, m, a, b, edges):
        obj=PriorityQueue()
        graph=[[] for _ in range(n)]
        for node1,node2,cost1,cost2 in edges:
            graph[node1-1].append([node2-1,cost1,cost2])
            graph[node2-1].append([node1-1,cost1,cost2])
        visited=[[1e9,1e9] for _ in range(n)]
        obj.put([0,a-1])
        visited[a-1][0]=0
        visited[a-1][1]=0
        while(not obj.empty()):
            cost,node=obj.get()
            if(node==b-1):
                return min(visited[node])
            else:
                for node1,cost1,cost2 in graph[node]:
                    if(visited[node1][1]>cost2+visited[node][0]):
                        visited[node1][1]=cost2+visited[node][0]
                        obj.put([cost2+visited[node][0],node1])
                    if(visited[node1][0]>cost1+visited[node][0]):
                        visited[node1][0]=cost1+visited[node][0]
                        obj.put([visited[node1][0],node1])
                    if(visited[node1][1]>cost1+visited[node][1]):
                        visited[node1][1]=cost1+visited[node][1]
                        obj.put([visited[node1][1],node1])
        return -1 


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys 
sys.setrecursionlimit(10**6) 
from heapq import *

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n,m=map(int,input().split())
        a,b=map(int,input().split())
        edges = []
        for i in range(m):
            edge = list(map(int,input().split()))
            edges.append(edge)
        
        ob = Solution()
        print(ob.shortestPath(n,m,a,b,edges))
# } Driver Code Ends