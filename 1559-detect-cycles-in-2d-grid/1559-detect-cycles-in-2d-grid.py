class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        m=len(grid)
        n=len(grid[0])
        par=[i for i in range(m*n)]
        rank=[0 for _ in range(m*n)]
        for i in range(m):
            for j in range(n):
                if(j+1<n and grid[i][j]==grid[i][j+1]):
                    node1=(i*n)+j
                    node2=node1+1
                    p1=self.find(par,node1)
                    p2=self.find(par,node2)
                    if(p1==p2):
                        return True
                    self.union(p1,p2,rank,par)
                if(i+1<m and grid[i+1][j]==grid[i][j]):
                    node1=(i*n)+j
                    node2=node1+n
                    p1=self.find(par,node1)
                    p2=self.find(par,node2)
                    if(p1==p2):
                        return True
                    self.union(p1,p2,rank,par)
        return False
    def union(self,p1,p2,rank,par):
        if(rank[p1]==rank[p2]):
            rank[p1]+=1
        if(rank[p1]>rank[p2]):
            par[p2]=p1
        else:
            par[p1]=p2
    def find(self,par,node):
        if(par[node]==node):
            return node
        par[node]=self.find(par,par[node])
        return par[node]