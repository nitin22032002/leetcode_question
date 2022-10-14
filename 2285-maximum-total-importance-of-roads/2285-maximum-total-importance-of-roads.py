class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        visited=[-1 for _ in range(n)]
        graph=[[] for _ in range(n)]
        for item in roads:
            a,b=item
            graph[a].append(b)
            graph[b].append(a)
        for i in range(n):
            if(visited[i]==-1):
                self.dfs(graph,i,visited,-1)
        # print(visited)
        visited.sort(reverse=True)
        ans=0
        start=n
        for item in visited:
            ans+=(item*start)
            start-=1
        return ans
    def dfs(self,graph,node,visited,par):
        if(visited[node]!=-1):
            visited[node]+=1
            return
        else:
            if(par!=-1):
                visited[node]=1
            else:
                visited[node]=0
            for item in graph[node]:
                self.dfs(graph,item,visited,node)
            return