#User function Template for python3
from queue import Queue
class Solution:
    def shortestXYDist(self, grid, N, M):
        obj=Queue()
        visited=[[False for _ in range(M)] for __ in range(N)]
        for i in range(N):
            for j in range(M):
                if(grid[i][j]=="X"):
                    visited[i][j]=True
                    obj.put([i,j,0])
        while(not obj.empty()):
            i,j,cost=obj.get()
            if(grid[i][j]=="Y"):return cost
            for i1,j1 in [[i+1,j],[i,j+1],[i-1,j],[i,j-1]]:
                if(i1>=0 and i1<N and j1>=0 and j1<M and not visited[i1][j1]):
                    visited[i][j1]=True
                    obj.put([i1,j1,cost+1])
        return -1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N,M=map(int,input().split())
        grid = []
        for i in range(N):
            ch = list(map(str,input().split()))
            grid.append(ch)
            
        ob = Solution()
        print(ob.shortestXYDist(grid,N,M))
# } Driver Code Ends