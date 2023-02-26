#User function Template for python3

import collections
from collections import deque
from collections import defaultdict

class Solution:
    def findNumberOfGoodComponent(self, V, adj):
        visited=[False]*V
        call=[False]*V
        ans=0
        for i in range(V):
            if(not visited[i]):
                nodes=self.get(adj,i,visited)
                r=self.isConnected(adj,i,call,nodes)
                if(r!=-1):
                    ans+=1
        return ans
    def get(self,graph,node,visited):
        if(visited[node]):
            return 0
        visited[node]=True
        ans=1
        for node1 in graph[node+1]:
            ans+=self.get(graph,node1-1,visited)
        return ans
    def isConnected(self,graph,node,visited,nodes):
        if(visited[node]):
            return 0
        visited[node]=True
        for node1 in graph[node+1]:
            a=self.isConnected(graph,node1-1,visited,nodes)
            if(a==-1):
                return -1
        if(len(graph[node+1])!=nodes-1):
            return -1
        return 1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

from sys import stdin, stdout
if __name__ == '__main__':
    test_cases = int(input())
    for _ in range (test_cases):
        E, V = map(int, input().split())
        adj = [[] for _ in range(V+1)]
        for _ in range(E):
            a,b = map(int, input().split())
            adj[a].append(b)
            adj[b].append(a)
            
        res = Solution().findNumberOfGoodComponent(V, adj)
        print(res)
# } Driver Code Ends