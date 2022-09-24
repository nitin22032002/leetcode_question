class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        graph=[[0 for _ in range(n)] for _ in range(n)]
        paths=[0 for _ in range(n)]
        for item in roads:
            graph[item[0]][item[1]]=1
            graph[item[1]][item[0]]=1
            paths[item[0]]+=1
            paths[item[1]]+=1
        # print(paths,graph)
        ans=0
        for i in range(n):
            for j in range(i+1,n):
                ans=max(ans,paths[i]+paths[j]-graph[i][j])
        return ans