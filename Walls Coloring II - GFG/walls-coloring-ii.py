#User function Template for python3

class Solution:
    def minCost(self, costs) -> int:
        n,k=len(costs),len(costs[0])
        if(n>1 and k<=1):
            return -1
        m1=[0,0]
        m2=[1,0]
        dp=[0 for _ in range(k)]
        for i in range(n):
            for j in range(k):
                if(j==m1[0]):
                    dp[j]=costs[i][j]+m2[1]
                else:
                    dp[j]=costs[i][j]+m1[1]
            m1=[0,dp[0]]
            if(k>=2):
                m2=[1,dp[1]]
            for j in range(1,k):
                if(m1[1]>=dp[j]):
                    m2=[m1[0],m1[1]]
                    m1=[j,dp[j]]
                elif(m2[1]>dp[j]):
                    m2=[j,dp[j]]
        return m1[1]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

from typing import List


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
        
        n, m = map(int, input().split())
        
        
        costs=IntMatrix().Input(n, m)
        
        obj = Solution()
        res = obj.minCost(costs)
        
        print(res)
# } Driver Code Ends