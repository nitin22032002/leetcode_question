class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        graph=[[] for _ in range(n)]
        for item in edges:
            a,b=item
            graph[a].append(b)
            graph[b].append(a)
        visited=[False for _ in range(n)]
        a,b=self.get(graph,hasApple,visited,0)
        if(a):
            b-=2
        return b
    def get(self,graph,apple,visited,node):
        visited[node]=True
        status=False
        cost=0
        for item in graph[node]:
            if(not visited[item]):
                a,b=self.get(graph,apple,visited,item)
                cost+=b
                status=status or a
        # print(node,status,cost)
        if(status or apple[node]):
            cost+=2
            status=True
        else:
            status=False
            cost=0
        return [status,cost]