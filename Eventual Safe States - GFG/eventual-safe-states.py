#User function Template for python3

from typing import List

class Solution:    
    def eventualSafeNodes(self, V : int, adj : List[List[int]]) -> List[int]:
        
        visited=[False]*V
        isSafe=[False]*V
        ans=[]
        for i in range(V):
            if(self.get(adj,i,visited,isSafe)):
                ans.append(i)
        return ans
            
    def get(self,graph,node,visited,isSafe):
        if(visited[node]):
            return isSafe[node]
        visited[node]=True
        status=True
        for item in graph[node]:
            status=status and self.get(graph,item,visited,isSafe)
        isSafe[node]=status
        return status



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    T = int(input())
    for t in range(T):
        
        V, E = map(int, input().strip().split())
        adj = [[] for i in range(V)]
        for i in range(E):
            u, v = map(int, input().strip().split())
            adj[u].append(v)
        obj = Solution()
        ans = obj.eventualSafeNodes(V, adj)
        for nodes in ans:
            print(nodes, end = ' ')
        print()
            


# } Driver Code Ends