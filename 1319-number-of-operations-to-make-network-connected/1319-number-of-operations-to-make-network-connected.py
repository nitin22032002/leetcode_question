class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if(len(connections)<(n-1)):
            return -1
        graph=[[] for _ in range(n)]
        for item in connections:
            a,b=item
            graph[a].append(b)
            graph[b].append(a)
        visited=[False for _ in range(n)]
        ans=0
        for i in range(n):
            if(not visited[i]):
                ans+=1
                self.dfs(graph,i,visited)
        return ans-1
    def dfs(self,graph,node,visited):
        if(visited[node]):
            return
        else:
            visited[node]=True
            for item in graph[node]:
                self.dfs(graph,item,visited)
            
    