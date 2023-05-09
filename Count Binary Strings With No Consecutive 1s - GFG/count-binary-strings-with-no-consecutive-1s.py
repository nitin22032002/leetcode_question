#User function Template for python3
class Solution: 
    def countStrings(self, n):
        self.mod=int(1e9+7)
        if(n==1):return 2
        elif(n==2):return 3
        else:
            mat=self.solve([[1,1],[1,0]],n-2)
            ans=mat[0][0]*3+mat[0][1]*2
            ans%=self.mod
            return ans
    def solve(self,mat,n):
        if(n==1):return mat
        x=self.solve(mat,n//2)
        if(n%2==0):
            return self.matrixMultiply(x,x)
        else:
            return self.matrixMultiply(self.matrixMultiply(x,x),mat)
    def matrixMultiply(self,mat1,mat2):
        ans=[[0,0],[0,0]]
        ans[0][0]=(mat1[0][0]*mat2[0][0])+(mat1[0][1]*mat2[1][0])
        ans[0][1]=(mat1[0][0]*mat2[0][1])+(mat1[0][1]*mat2[1][1])
        ans[1][0]=(mat1[1][0]*mat2[0][0])+(mat1[1][1]*mat2[1][0])
        ans[1][1]=(mat1[1][0]*mat2[0][1])+(mat1[1][1]*mat2[1][1])
        for i in range(2):
            for j in range(2):
                ans[i][j]%=self.mod
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3
#Initial Template for Python 3

if __name__ == '__main__':
    
    T = int(input())
    while T > 0: 
        
        ob = Solution()
        print(ob.countStrings(int(input())))
        
        T -= 1
# } Driver Code Ends