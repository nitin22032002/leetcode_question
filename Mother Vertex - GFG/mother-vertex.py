
class Solution:
    
    #Function to find a Mother Vertex in the Graph.
	def findMotherVertex(self, V, adj):
		visited=[False]*V
	    for i in range(V):
	        if(visited[i]==False):
	            self.get(adj,i,visited)
	            vertex=i
	    vis=[False]*V
	    self.get(adj,vertex,vis)
	    for item in vis:
	        if(not item):return -1
	    return vertex
	def get(self,graph,node,visited):
	    if(visited[node]):
	        return
	    else:
	        visited[node]=True
	        for item in graph[node]:
	            self.get(graph,item,visited)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys 

sys.setrecursionlimit(10**6) 
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
		obj = Solution()
		ans = obj.findMotherVertex(V, adj)
		print(ans)
# } Driver Code Ends