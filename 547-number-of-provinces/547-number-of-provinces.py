class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited=[False for _ in range(len(isConnected))]
        ans=0
        for i in range(len(isConnected)):
            ans+=self.get(isConnected,visited,i)
        return ans
    
    def get(self,graph,visited,start):
        if(visited[start]):
            return 0
        else:
            visited[start]=True
            for i in range(len(graph)):
                if(graph[start][i]==1):
                    self.get(graph,visited,i)
            return 1