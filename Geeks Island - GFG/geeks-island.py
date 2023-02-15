#User function Template for python3
from queue import Queue
class Solution():
    def water_flow(self, heights, n, m):
        obj=Queue()
        dp=[[[False,False] for _ in range(m)] for __ in range(n)]
        for i in range(n):
                dp[i][0][0]=True
                dp[i][m-1][1]=True
                obj.put([i,0,0])
                obj.put([i,m-1,1])
        for i in range(m):
                dp[0][i][0]=True
                obj.put([0,i,0])
                obj.put([n-1,i,1])
                dp[n-1][i][1]=True
        # print(dp)
        while(not obj.empty()):
            i,j,c=obj.get()
            for i1,j1 in [[i+1,j],[i-1,j],[i,j+1],[i,j-1]]:
                if not(i1>=n or j1>=m or i1<0 or j1<0 or dp[i1][j1][c] or heights[i][j]>heights[i1][j1]):
                    dp[i1][j1][c]=True
                    obj.put([i1,j1,c])
        ans=0
        for i in range(n):
            for j in range(m):
                if(dp[i][j][0] and dp[i][j][1]):
                    ans+=1
        return ans
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)
if __name__ == "__main__":
    for _ in range(int(input())):
        n,m = map(int, input().split())
        mat = []
        for i in range(n):
            tmp = [int(i) for i in input().split()]
            mat.append(tmp)
        print(Solution().water_flow(mat, n, m))
# } Driver Code Ends