#User function Template for python3
import sys
sys.setrecursionlimit(10**8)
from typing import List

class Solution:    
    def numberOfEnclaves(self, grid: List[List[int]]) -> int:
        ans=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                a,b=self.get(grid,i,j)
                if(not a):
                    ans+=b
        return ans
    
    def get(self,grid,i,j):
        if(i>=len(grid) or j>=len(grid[0]) or i<0 or j<0):
            return [True,0]
        elif(grid[i][j]==0):
            return [False,0]
        else:
            grid[i][j]=0
            ans=1
            status=False
            for i1,j1 in [[i+1,j],[i-1,j],[i,j+1],[i,j-1]]:
                a,b=self.get(grid,i1,j1)
                status=status or a
                ans+=b
            return [status,ans]


#{ 
 # Driver Code Starts
#Initial Template for Python 3


if __name__ == "__main__":
    for _ in range(int(input())):
        n, m = map(int,input().strip().split())
        grid = []
        for i in range(n):
            grid.append([int(i) for i in input().strip().split()])

        obj=Solution()
        print(obj.numberOfEnclaves(grid))
# } Driver Code Ends