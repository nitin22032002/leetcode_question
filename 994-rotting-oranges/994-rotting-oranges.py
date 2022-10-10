from queue import Queue
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        obj=Queue()
        dp=[[m*n+1 for _ in range(n)] for __ in range(m)]
        for i in range(m):
            for j in range(n):
                if(grid[i][j]==2):
                    dp[i][j]=0
                    obj.put([[i,j],0])
        ans=0
        while(not obj.empty()):
            pos,cost=obj.get()
            ans=max(ans,cost)
            i,j=pos
            grid[i][j]=2
            if(i-1>=0 and grid[i-1][j]!=0 and dp[i-1][j]>cost+1):
                dp[i-1][j]=cost+1
                obj.put([[i-1,j],cost+1])
            if(j-1>=0 and grid[i][j-1]!=0 and dp[i][j-1]>cost+1):
                dp[i][j-1]=cost+1
                obj.put([[i,j-1],cost+1])
            if(i+1<m and grid[i+1][j]!=0 and dp[i+1][j]>cost+1):
                dp[i+1][j]=cost+1
                obj.put([[i+1,j],cost+1])
            if(j+1<n and grid[i][j+1]!=0 and dp[i][j+1]>cost+1):
                dp[i][j+1]=cost+1
                obj.put([[i,j+1],cost+1])
        for i in range(m):
            for j in range(n):
                if(grid[i][j]==1):
                    return -1
        return ans
    