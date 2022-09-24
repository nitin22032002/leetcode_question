# from numpy import array
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m,n=len(matrix),len(matrix[0])
        dp=[[0 for _ in range(n)] for __ in range(m)]
        for i in range(m):
            if(matrix[i][0]=="1"):
                dp[i][0]=1
        for i in range(n):
            if(matrix[0][i]=="1"):
                dp[0][i]=1
        for i in range(1,m):
            for j in range(1,n):
                if(matrix[i][j]=="1"):
                    a=int(pow(dp[i-1][j-1],0.5))
                    b=0
                    k=i-1
                    while(b<=a):
                        if(matrix[k][j]=="1"):
                            b+=1
                        else:
                            break
                        k-=1
                    a=min(a,b)
                    b=0
                    k=j-1
                    while(b<=a):
                        if(matrix[i][k]=="1"):
                            b+=1
                        else:
                            break
                        k-=1
                    a=min(a,b)
                    dp[i][j]=(a+1)*(a+1)
        # print(array(dp))           
        ans=0
        for i in range(m):
            for j in range(n):
                ans=max(ans,dp[i][j])
        return ans