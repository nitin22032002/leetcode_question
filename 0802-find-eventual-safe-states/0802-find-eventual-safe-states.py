class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        visited=[False for _ in range(len(graph))]
        isSafe=[False for _ in range(len(graph))]
        for i in range(len(graph)):
            if(not visited[i]):
                self.dfs(graph,i,visited,isSafe)
        
        ans=[]
        for i in range(len(isSafe)):
            if(isSafe[i]):
                ans.append(i)
        return ans
    def dfs(self,graph,node,visited,isSafe):
        if(visited[node]):
            return isSafe[node]
        else:
            visited[node]=True
            status=True
            for item in graph[node]:
                status=status and self.dfs(graph,item,visited,isSafe)
            isSafe[node]=status
            return status