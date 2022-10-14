class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color=[-1 for _ in range(len(graph))]
        for i in range(len(graph)):
            if(color[i]==-1):
                if(not self.bipartite(graph,i,color,0)):
                    return False
        return True
    def bipartite(self,graph,node,visited,color):
        if(visited[node]!=-1):
            return visited[node]==color
        else:
            visited[node]=color
            if(color==0):
                color=1
            else:
                color=0
            for item in graph[node]:
                if(not self.bipartite(graph,item,visited,color)):
                    return False
            return True