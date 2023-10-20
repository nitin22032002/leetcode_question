from typing import List

class Solution:
    def largestIsland(self, grid : List[List[int]]) -> int:
        start=2
        d={}
        ans=0
        for i in range(len(grid)):
            for j in range(len(grid)):
                x=self.find(grid,i,j,start)
                if(x!=0):
                    d[start]=x
                    start+=1
                    ans=max(ans,x)
        for i in range(len(grid)):
            for j in range(len(grid)):
                if(grid[i][j]==0):
                    c=1
                    r=set()
                    for i1,j1 in [[i+1,j],[i-1,j],[i,j+1],[i,j-1]]:
                        if(i1<0 or j1<0 or i1>=len(grid) or j1>=len(grid) or grid[i1][j1]==0 or grid[i1][j1] in r):
                            continue
                        r.add(grid[i1][j1])
                        c+=d[grid[i1][j1]]
                    ans=max(ans,c)
        return ans
                
    
    def find(self,grid,i,j,k):
        if(i<0 or j<0 or i>=len(grid) or j>=len(grid) or grid[i][j]!=1):
            return 0
        else:
            grid[i][j]=k
            ans=1
            for i1,j1 in [[i+1,j],[i-1,j],[i,j+1],[i,j-1]]:
                ans+=self.find(grid,i1,j1,k)
            return ans
        







#{ 
 # Driver Code Starts

class IntMatrix:
    def __init__(self) -> None:
        pass
    def Input(self,n,m):
        matrix=[]
        #matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix
    def Print(self,arr):
        for i in arr:
            for j in i:
                print(j,end=" ")
            print()

if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        
        grid=IntMatrix().Input(n,n)
        
        obj = Solution()
        res = obj.largestIsland(grid)
        
        print(res)
# } Driver Code Ends